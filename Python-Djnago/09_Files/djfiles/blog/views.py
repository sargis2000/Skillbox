import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import BlogForm
from .models import BlogPost, Picture


@login_required
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('blog_view')
    return render(request, 'blog/create_blog.html', {'form': form})


def blog_view(request):
    return render(request, 'blog/blogview.html', {'content': BlogPost.objects.order_by('-created_at')})


class BlogView(DetailView):
    template_name = 'blog/detail_view.html'
    context_object_name = 'item'
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pictures'] = Picture.objects.filter(news_id=kwargs['object'].id)
        return context


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="posts.csv"'
    posts = BlogPost.objects.all()
    writer = csv.writer(response)
    for post in posts:
        writer.writerow([post.content, post.created_at])
    return response
