from django.urls import path
from .views import ProductListView, buy, popularitems

urlpatterns = [
    path('', ProductListView.as_view(), name='Shop_url'),
    path('buy/',  buy, name='buy_url'),
    path('popular-items/', popularitems, name='popularitems')
]