from django.urls import path, include
from .views import register, additional_view, account_view, validate_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('additional_info/', additional_view, name='additional_view'),
    path('profile/', account_view, name='accountview'),
    path('validate_user', validate_user, name='validate_user')
]