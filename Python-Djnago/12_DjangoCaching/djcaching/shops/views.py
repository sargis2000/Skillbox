from django.shortcuts import render
from django.utils.translation import gettext as _


def shop_view(request):
    return render(request, 'shops/shops.html', {'shops': _([f'shop example {n}' for n in range(100000)])})