from django.shortcuts import render, redirect
from . forms import NewUserForm
from django.contrib.auth import login


def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user=user)
            return redirect('/')
    return render(request, 'registration/register.html', {'form': form})