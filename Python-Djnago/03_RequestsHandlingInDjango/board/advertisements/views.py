from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

counter = 0


class AdvertisementList(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        self.advertisements_1 = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        self.__categories = ('Cat1', 'Cat2', 'Cat3') * 10
        self.__region = ('Reg1', 'reg2') * 10

    def get(self, request):
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': self.advertisements,
                                                                          'advertisements_1': self.advertisements_1,
                                                                          'categories': self.__categories,
                                                                          'region': self.__region})


class GreetingView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__context = {'advertisements{}'.format(i): [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
            for i in range(1, 5)}

    def get(self, request):
        global counter
        counter += 1
        return render(request, 'advertisements/adv_list_based.html', {'context': self.__context,
                                                                      'Calls': counter})

    @staticmethod
    def post(request):
        global counter
        counter += 1
        return render(request, 'advertisements/adv_list_based.htm',
                      {'context': 'запрос на создание новой записи успешно выполнен.',
                       'Calls': counter}
                      )


class ContactView(TemplateView):
    template_name = 'advertisements/Contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'any address'
        context['phone_number'] = '+374980509768'
        return context


class AboutView(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comp_name'] = 'название компани'
        context['text'] = 'текст с описанием'
        return context
