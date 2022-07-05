from django.shortcuts import render


def index(request):
    return render(request, 'Shop/Home.html')


def courses(request, **kwargs):
    return render(request, 'Shop/Course.html', kwargs)
