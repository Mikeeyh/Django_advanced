from django.contrib import admin
from django.contrib.auth import get_user_model

from custom_auth.accounts.forms import AccountUserCreationForm, AccountUserChangeForm

""" 
We should add our admin model here because 
when we use a custom 'user' model this is not 
automatically shown in admin administration
"""


UserModel = get_user_model()  # this is working even with custom or built in user

# This is for our 1. way to extend a 'User' model:


# @admin.register(UserModel)
# class UserModelAdmin(admin.ModelAdmin):
#     pass


# This is for our 2.2. way to extend a 'User' model:
from django.contrib.auth import admin as auth_admin


@admin.register(UserModel)
class UserModelAdmin(auth_admin.UserAdmin):
    list_display = ('email', 'is_superuser', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)

    form = AccountUserChangeForm
    add_form = AccountUserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups',
                                    'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


"""
ERRORS: (without list_display added)
<class 'custom_auth.accounts.admin.UserModelAdmin'>: (admin.E033) The value of 'ordering[0]' refers to 'username', which is not a field of 'accounts.AccountUser'.
<class 'custom_auth.accounts.admin.UserModelAdmin'>: (admin.E108) The value of 'list_display[0]' refers to 'username', which is not a callable, an attribute of 'UserModelAdmin', or an attribute or method on 'accounts.AccountUser'.
<class 'custom_auth.accounts.admin.UserModelAdmin'>: (admin.E108) The value of 'list_display[2]' refers to 'first_name', which is not a callable, an attribute of 'UserModelAdmin', or an attribute or method on 'accounts.AccountUser'.
<class 'custom_auth.accounts.admin.UserModelAdmin'>: (admin.E108) The value of 'list_display[3]' refers to 'last_name', which is not a callable, an attribute of 'UserModelAdmin', or an attribute or method on 'accounts.AccountUser'.
"""

"""
FieldError at /admin/accounts/accountuser/2/change/
Unknown field(s) (username, last_name, first_name) specified for AccountUser. Check fields/fieldsets/exclude attributes of class UserModelAdmin.
SOLVE IT -----> 'add_form = AccountUserCreationForm' and 'form = AccountUserChangeForm'
"""

"""
FieldError at /admin/accounts/accountuser/2/change/
Unknown field(s) (last_name, first_name, username) specified for AccountUser. Check fields/fieldsets/exclude attributes of class UserModelAdmin.
SOLVE IT -----> 
    'add_form = AccountUserCreationForm'
    'form = AccountUserChangeForm'
    Add: 'Fieldsets' and 'add_fieldsets'
"""
