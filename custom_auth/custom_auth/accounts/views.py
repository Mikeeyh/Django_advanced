from django import forms
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms

from custom_auth.accounts.forms import AccountUserCreationForm
from custom_auth.accounts.models import Profile

UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy("index")


# class AccountUserCreationForm(auth_forms.UserCreationForm):  # FOR 1. WAY TO MAKE CUSTOM USER:
#     class Meta(auth_forms.UserCreationForm.Meta):
#         model = UserModel  # instead of the built-in -> 'model = User'
#         # fields = auth_forms.UserCreationForm.Meta.fields + ("age",)  # adding fields to registration form


# We moved the form for 2.1. and 2.2. in forms.py


class RegisterUserView(views.CreateView):
    form_class = AccountUserCreationForm  # instead of the built-in -> 'auth_forms.UserCreationForm'
    template_name = 'accounts/register.html'
    success_url = reverse_lazy("index")


"""
FOR 1. Way:
This code will show us an error when we click on 'register' button:

    AttributeError at /accounts/register/
    Manager isn't available; 'auth.User' has been swapped for 'accounts.AccountUser'
    
    |----->
    This is because the built-in 'UserCreationForm' uses a hardcode 'User' but we have our custom 'AccountUser'.
    So, in this case, we need to add a new form which will inherit a built-in form.
    |------>
    We add:
    
        UserModel = get_user_model()
        
    class AccountUserCreationForm(auth_forms.UserCreationForm):
        class Meta(auth_forms.UserCreationForm.Meta):
            model = UserModel
"""

"""
For 2.2 way, we just remove AccountUserCreationForm and RegisterUserView 
in order to make migrations, then we revert them back
"""