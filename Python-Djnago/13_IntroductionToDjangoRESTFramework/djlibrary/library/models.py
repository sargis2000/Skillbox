from django.db import models


class Author(models.Model):
    """ Model For Authors"""
    f_name = models.CharField(max_length=200, verbose_name='Author Name')
    l_name = models.CharField(max_length=200, verbose_name='Last Name')
    date_of_birth = models.DateField(verbose_name='Date of birth:')


class Book(models.Model):
    """ Model for Books"""
    title = models.CharField(max_length=700, verbose_name='Title')
    isbn = models.IntegerField(verbose_name='isbn')
    issue_year = models.DateField(verbose_name='year of issue')
    pages_count = models.IntegerField(verbose_name='Pages count')
    author = models.ForeignKey('Author', verbose_name='Author', related_name='author', on_delete=models.CASCADE)