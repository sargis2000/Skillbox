from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_filter = ['verified', 'country']
    list_display = ['first_name', 'last_name', 'phone', 'country', 'verified', 'user_id']
