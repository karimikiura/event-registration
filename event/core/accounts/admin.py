from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from.forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
#     list_display = ['username', 'email', ]

    fieldsets = (
        *UserAdmin.fieldsets,
        ( 'User Information', {
            'fields': (
                'bio',
                'avatar',
                'hackthon_participant',
            ),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
