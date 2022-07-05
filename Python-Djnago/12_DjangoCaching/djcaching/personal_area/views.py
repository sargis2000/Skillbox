from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


@login_required
def personal_area(request):
    # low level cache API
    cache.set('promotions', [f'promution ex{n}' for n in range(50)], 60 * 2)
    cache.set('offers', [f'Offer {n}' for n in range(50)], 60 * 2)

    return render(request=request, template_name='personal_area/personal_page.html', context={'balance': 1000,
                                                                                              'promotions': cache.get(
                                                                                                  'promotions'),
                                                                                              'offers': cache.get(
                                                                                                  'offers'),
                                                                                              'purchase_history': [
                                                                                                  f'history {n}' for n
                                                                                                  in range(100)
                                                                                              ]})
