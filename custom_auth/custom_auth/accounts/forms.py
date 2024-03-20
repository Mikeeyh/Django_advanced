from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import UserChangeForm

from custom_auth.accounts.models import Profile


UserModel = get_user_model()


class AccountUserChangeForm(auth_forms.UserChangeForm):  # add this class too, then add it to the admin.py too
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'


class AccountUserCreationForm(auth_forms.UserCreationForm):  # FOR 2.1. and 2.2 WAY TO MAKE CUSTOM USER:
    age = forms.IntegerField()
    # Other fields of 'Profile'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        # fields = auth_forms.UserCreationForm.Meta.fields + ("age",)  # adding fields to registration form
        fields = (UserModel.USERNAME_FIELD,)  # for 2.2 way, remove it for 2.1 way

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            age=self.cleaned_data["age"],
        )

        if commit:
            profile.save()
        return user  # returns the 'user' we created
