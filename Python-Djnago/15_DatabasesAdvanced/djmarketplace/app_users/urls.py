from django.urls import path, include
from .views import user_profile, update_balance
import logging




urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', user_profile, name='profile_url'),
    path('update_balance/', update_balance, name='update_balance',)
]