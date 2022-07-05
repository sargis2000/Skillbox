from django.urls import path
from .views import cart_add, cart_remove, cart_detail


urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('cart-add/<int:product_id>, <int:magazine_id>', cart_add, name='cart_add'),
    path('cart-remove/<int:product_id>,<int:magazine_id>', cart_remove, name='cart_remove'),
]