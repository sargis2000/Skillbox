from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', verbose_name='user')
    balance = models.BigIntegerField(default=0)

    class Meta:
        db_table = 'Users_Profiles'

    def __str__(self):
        return self.user.first_name
