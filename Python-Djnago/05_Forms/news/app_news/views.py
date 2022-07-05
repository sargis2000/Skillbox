from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from .forms import CreateNewsForm, CommentForm
from django.http import HttpResponseRedirect


class NewsView(ListView):
    queryset = News.objects.filter(status='p')
    template_name = 'app_news/news_listview.html'
    context_object_name = 'news'


class NewsDetailView(DetailView):
    model = News
    template_name = 'app_news/news_detailview.html'
    context_object_name = 'news'

    def post(self, request, pk):
        form = CommentForm(self.request.POST or None, is_authenticated=self.request.user.is_authenticated)
        if form.is_valid():
            if 'user_name' in request.POST:
                user_name = request.POST['user_name'] + '---> Anonymous User'
            else:
                user_name = self.request.user.get_full_name()
            comment = Comment.objects.create(user_name=user_name,
                                             comment=self.request.POST['comment'],
                                             news=News.objects.get(id=pk),)
            comment.save()
        return HttpResponseRedirect(f'/news/{pk}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.all().filter(news_id=self.kwargs.get('pk')).order_by('created_on')
        context['form'] = CommentForm(is_authenticated=self.request.user.is_authenticated)
        return context


def create_news(request):
    message = ''
    if request.method == 'POST':
        form = CreateNewsForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Created successfully'
        else:
            message = 'correct bellow errors'
            return render(request, 'app_news/createnews.html', {'form': form,
                                                                'message': message})
    return render(request, 'app_news/createnews.html', {'form': CreateNewsForm(),
                                                        'message': message})


def edit_news(request, news_id):
    message = ''
    product = News.objects.get(id=news_id)
    if request.method == "POST":
        form = CreateNewsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            message = 'Ssccessfully edited news'
    else:
        form = CreateNewsForm(instance=product)
    return render(request, 'app_news/edit.html', {'form': form, 'message': message})



