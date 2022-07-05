from django.urls import path
from . views import personal_area


urlpatterns = [
    path('', personal_area, name='personal_area')
]