from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='news_listview'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='detailnews'),
    path('createnews/', create_news, name='Create_news'),
    path('change_news_status/', publish_news, name='publish news'),
    path('search', search, name='search')
]
