from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Degree
from .models import Profile
from .models import School
from .models import User


# The @admin.register stuff is explained here:
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/ ...
#                                                       #the-register-decorator

# list_display is explained here:
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/ ...
#                                 #django.contrib.admin.ModelAdmin.list_display

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'program', 'grad_year', 'resume', 'searchable'
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('abbrev', 'name')


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass

"""Integrate with admin module."""


# https://www.fomfus.com/articles/
# how-to-use-email-as-username-for-django-authentication-removing-the-username
# #Register%20your%20new%20User%20model%20with%20Django%20admin
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name',)
