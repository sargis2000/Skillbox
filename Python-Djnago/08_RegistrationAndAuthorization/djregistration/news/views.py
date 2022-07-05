from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect,HttpResponse
from .forms import CreateNewsForm, PublishNews, CommentForm, SearchForm
from django.contrib.auth.decorators import permission_required, user_passes_test
from app_users.views import create_permissions, Moderators, Validated_user
from .models import News, Comment , Tags


# def group_required(*group_names):
#     """Requires user membership in at least one of the groups passed in."""
#     def in_groups(user):
#         if user.is_authenticated():
#             if user.groups.filter(name__in=group_names) or user.is_superuser or user.is_stuff:
#                 return True
#         return False
#     return user_passes_test(in_groups, login_url='403')

Validated_user.permissions.add(create_permissions(News, 'can_create_news', 'Can create news'))
Moderators.permissions.add(create_permissions(News, 'can_publish_news', 'Can publish news'))


class NewsView(ListView):
    queryset = News.objects.filter(status='p')
    template_name = 'news/news_listview.html'
    context_object_name = 'news'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_form'] = SearchForm()
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detailview.html'
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


@permission_required('news.can_create_news')
def create_news(request):
    message = ''
    if request.method == 'POST':
        form = CreateNewsForm(request.POST)
        if form.is_valid():
            tag_instance, _ = Tags.objects.get_or_create(tag_name=request.POST['tag'],
                                                         slug=request.POST['tag'])
            News.objects.get_or_create(
                name=form.cleaned_data['name'],
                context=form.cleaned_data['context'],
                tag=tag_instance
            )
            message = 'Created successfully'
        else:
            message = 'correct bellow errors'
            return render(request, 'news/createnews.html', {'form': form,
                                                            'message': message})
    return render(request, 'news/createnews.html', {'form': CreateNewsForm(),
                                                    'message': message})


@permission_required('news.can_publish_news')
def publish_news(request):
    form = PublishNews()
    if request.method == "POST":
        form = PublishNews(request.POST)
        if form.is_valid():
            for i in form.cleaned_data:
                if form.cleaned_data[i]:
                    News.objects.filter(id=i[-1]).update(status='p')
                else:
                    News.objects.filter(id=i[-1]).update(status='d')
            return redirect('news_listview')
        else:
            return HttpResponse('Some error here not time for this """""""""""""""""""""SSSSSSSSs')
    return render(request, 'news/publish_news.html', {'form': form})


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data != ' ':
                try:
                    result = News.objects.filter(tag_id=Tags.objects.get(tag_name=form.cleaned_data['search']))
                except:
                    result = 'CAnt find anything'
                finally:
                    return render(request, 'news/news_listview.html', {'search_result': result,
                                                                       'search_form': SearchForm()})
    return redirect('news_listview')
