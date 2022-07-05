from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import AdditionalInfoForm
from django.http import HttpResponse
# Create your views here.


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request=request, template_name='blog/about_me.html',
                          context={'form': AdditionalInfoForm()})
    return render(request=request, template_name='registration/register.html', context={'form': form})


def about_me(request):
    add_form = AdditionalInfoForm(request.POST)
    if add_form.is_valid():
        User.objects.filter(id=request.user.id).update(last_name=request.POST['last_name'],
                                                       first_name=request.POST['first_name'])
        return HttpResponse('name and last name updated!!!!!!!!')
    return render(request, 'blog/about_me.html', {'form': add_form})

