from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='news_listview'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='detailnews'),
    path('createnews', create_news, name='Create_news'),
    path('edit/<int:news_id>', edit_news,  name='edit_data')
]
