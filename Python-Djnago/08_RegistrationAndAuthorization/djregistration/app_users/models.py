from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=100, verbose_name='last name')
    phone = PhoneNumberField(unique=True)
    country = CountryField()
    posted_news = models.IntegerField(default=0, editable=False)
    verified = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'Profile'
