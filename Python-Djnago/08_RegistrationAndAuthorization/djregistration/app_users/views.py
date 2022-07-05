from django.shortcuts import render, redirect
from .forms import UserRegistration, Additional, ValidateForm
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.models import User, Group, Permission, ContentType
from news.models import News
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


def create_permissions(perm_model, codename, name):
    # for validate
    content_type = ContentType.objects.get_for_model(perm_model)
    permission_validate_user, permission_validate_user_created = Permission.objects.get_or_create(
        codename=codename,
        name=name,
        content_type=content_type)
    return permission_validate_user


# creating groups
Simple_user, Simple_User_created = Group.objects.get_or_create(name='Simple Users')
Validated_user, Validated_user_created = Group.objects.get_or_create(name='Validated Users')
Moderators, Moderators_created = Group.objects.get_or_create(name='Moderators')

# add permissions for group
Moderators.permissions.add(create_permissions(Profile, 'can_validate_user', 'Can validate user', ))


def register(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return render(request, 'registration/additional_info.html', {'form': Additional(),
                                                                         'congratulation': 'You have registered!!!!!'})
        else:
            form.message = form.error_messages
    return render(request, 'registration/register.html', {'form': form})


def additional_view(request):
    if request.method == "POST":
        form = Additional(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            try:
                Profile.objects.create(user=user,
                                       first_name=form.cleaned_data['first_name'],
                                       last_name=form.cleaned_data['last_name'],
                                       phone=form.cleaned_data['phone'],
                                       country=form.cleaned_data['country'])
            except:
                Profile.objects.filter(user=user).update(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone=form.cleaned_data['phone'],
                    country=form.cleaned_data['country']
                )
            return redirect('/')
        form.message = form.errors
        return render(request, 'registration/additional_info.html', {'form': form})
    return HttpResponse('First you need to register')


def account_view(request):
    return render(request, 'profile.html', {'content': Profile.objects.get(user_id=request.user.id)})


@permission_required('app_users.can_validate_user')
def validate_user(request):
    form = ValidateForm()
    if request.method == 'POST':
        form = ValidateForm(request.POST)
        if form.is_valid():
            for i in form.cleaned_data:
                Profile.objects.filter(user_id=i[-1]).update(
                    verified=form.cleaned_data[i]
                )
                User.objects.get(id=i[-1]).groups.add(Validated_user)
        return redirect('/')
    return render(request, 'registration/validate_users.html', {'form': form})
