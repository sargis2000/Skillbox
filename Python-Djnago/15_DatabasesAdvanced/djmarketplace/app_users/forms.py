from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    def save(self, request):
        Profile.objects.get_or_create(user=request.user)
        user = User.objects.get(id=request.user.id)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class UpdateBalanceForm(forms.Form):
     balance = forms.IntegerField(help_text='balance')
