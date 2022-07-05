from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import *
import requests
import json


class AdvertisementsListView(ListView):
    model = Adv
    context_object_name = 'Adv'
    template_name = 'advertisements/advertisements.html'


class AdvertisementsDetailView(DetailView):
    model = Adv
    context_object_name = 'Adv'
    template_name = 'advertisements/advertisementsdetail.html'
    slug_field = 'adv_slug'

    @staticmethod
    def get_val():
        return json.loads(requests.get('https://api.exchangerate-api.com/v4/latest/USD').text)['rates']['RUB']

    def get_context_data(self, **kwargs):
        context = super(AdvertisementsDetailView, self).get_context_data(**kwargs)
        context['adv_price_usd'] = context['object'].adv_price * self.get_val()
        return context


