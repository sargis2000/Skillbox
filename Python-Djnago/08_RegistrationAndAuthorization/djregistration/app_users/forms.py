from django.contrib.auth import forms as auth_form
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegistration(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class Additional(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone', 'country', )


class ValidateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unverified = Profile.objects.filter(
                                        verified=0
                                    )
        for i in self.unverified:
            field_name = f'Profile {i.user} {i.first_name} {i.last_name} {i.phone}  {i.user_id}'
            self.fields[field_name] = forms.BooleanField(required=False)


