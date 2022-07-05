from django.urls import path
from .views import BooksAPIView,AuthorAPIView

urlpatterns = [
    path('api/authors/', AuthorAPIView.as_view()),
    path('api/books/', BooksAPIView.as_view())
]