from django.urls import path
from . views import *

urlpatterns = [
    path('advertisements', AdvertisementsListView.as_view(), name='advertisements'),
    path('advertisements/<slug:slug>/', AdvertisementsDetailView.as_view(), name='adv_detail_view')
]
