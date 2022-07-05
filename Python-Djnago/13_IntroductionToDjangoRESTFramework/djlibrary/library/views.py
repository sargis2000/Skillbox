from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BooksSerializer
from rest_framework import filters


class AuthorAPIView(generics.ListAPIView):
    """ API VIEW FOR AUTHORS """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['f_name']


class BooksAPIView(generics.ListAPIView):
    """ API VIEW FOR BOOKS """
    serializer_class = BooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__f_name', 'title']


def get_queryset(self):
    """
        Function to get Current query
        :param self: Used to represent the instance of the class
        :return queryset: Filtered Books list
    """
    queryset = Book.objects.all()
    symbol = self.request.query_params.get('symbol')
    pages_count = self.request.query_params.get('pages_count')
    if pages_count and symbol is not None:
        if symbol == '=':
            queryset = Book.objects.all().filter(pages_count=pages_count)
        elif symbol == '<':
            queryset = [i for i in Book.objects.all() if i.pages_count < int(pages_count)]
        elif symbol == '>':
            queryset = [i for i in Book.objects.all() if i.pages_count > int(pages_count)]
    return queryset
