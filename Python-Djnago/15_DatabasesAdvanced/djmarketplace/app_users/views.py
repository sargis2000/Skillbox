from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, UpdateBalanceForm


def user_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save(request)
            form.message = 'Done!!!'
            return redirect('profile_url')
        return render(request, 'account/profile.html', {'form': form})
    if request.method == 'GET':
        if Profile.objects.filter(user=request.user).exists():
            return render(request, 'account/profile.html', {'profile': Profile.objects.get(user=request.user)})
    return render(request, 'account/profile.html', {'form': form})


def update_balance(request):
    form = UpdateBalanceForm()
    if request.method == 'POST':
        form = UpdateBalanceForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.balance += form.cleaned_data['balance']
            profile.save()
            return redirect('profile_url')
    return render(request, 'account/profile.html', {'balance_form': form})


