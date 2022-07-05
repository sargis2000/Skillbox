from django.urls import path
from . views import BlogView, blog_view, create_blog, getfile

urlpatterns = [
    path('', blog_view, name='blog_view'),
    path('creat_news/', create_blog, name='creat_news'),
    path('blog_news/detailview/<int:pk>', BlogView.as_view(), name='detail_view'),
    path('downlod_posts/', getfile, name='getfile')
]