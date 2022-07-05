from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class AdvType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100, unique=True, verbose_name='Type name')
    type_slug = models.SlugField(verbose_name='slug')

    def __str__(self):
        return self.type_name


class AdvCreator(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(max_length=200)
    # pls run this pip install -r rec.txt
    author_phone_number = PhoneNumberField(unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'author'
        db_table = 'author'

    def __str__(self):
        return self.author_name


class Adv(models.Model):
    adv_id = models.AutoField(primary_key=True)
    adv_name = models.CharField(max_length=300, unique=True, verbose_name='Name')
    adv_slug = models.SlugField(verbose_name='slug', unique=True,)
    adv_context = models.TextField(verbose_name='Context')
    adv_price = models.IntegerField(verbose_name='Price')
    adv_created_on = models.DateTimeField(auto_now_add=True)
    adv_updates_on = models.DateTimeField(auto_now=True)
    adv_ends_on = models.DateTimeField(verbose_name='Ends on ->', default=timezone.now)
    adv_author = models.ForeignKey(AdvCreator, verbose_name='Author Name',
                                   related_name='foreign_author', on_delete=models.CASCADE)

    adv_type = models.ForeignKey(AdvType, verbose_name='Category', null=True, blank=True,
                                 related_name='foreign_type', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'advertisement'
        db_table = 'advertisement'

    def __str__(self):
        return self.adv_name




