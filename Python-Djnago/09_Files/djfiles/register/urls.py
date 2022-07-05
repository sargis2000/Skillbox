from django.urls import path, include
from . views import register,about_me


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('about_me/', about_me, name='about_me'),
]