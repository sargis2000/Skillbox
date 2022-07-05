from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdvertisementList.as_view(), name='advertisement_list'),
    path('based_view', views.GreetingView.as_view(), name='ClassBasedView'),
    path('сontacts', views.ContactView.as_view(), name='ContactView'),
    path('about', views.AboutView.as_view(), name='AboutView'),
]
