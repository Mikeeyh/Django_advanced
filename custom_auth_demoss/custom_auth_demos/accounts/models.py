from django.contrib.auth import get_user_model, models as auth_models
from django.db import models

"""
1. Use the default user as-is
2. Extend the default user and add more stuff (Extend the 'AbstractUser' class)
3. Rewrite the whole user (Extend the 'AbstractBaseUser' class)
"""

"""
TWO WAYS TO EXTEND THE USER MODEL:

2. Extend the user through a One-to-One relationship with 'Profile' model:
    - Add 'age' field.
    - Add 'gender' field.

2.1 Use the built-in user for auth
2.2 Create our own user model

# Better at:
    - Easier migration to other auth model in the future
    - No need to rewrite Django auth system
"""

UserModel = get_user_model()

"""
1. Extend the built-in user model through 'AbstractUser':
    - Add 'age' field.
    - Add 'gender' field.

# Better at:
    - Simpler
    - No need to rewrite Django auth system
"""


class AccountUser(auth_models.AbstractUser):
    age = models.PositiveIntegerField(
        blank=False,
        null=False,
    )


class AccountsUserProxy(UserModel):
    class Meta:
        proxy = True
        ordering = ('first_name',)

    def some_custom_behavior(self): ...


print(UserModel.objects.all())  # ordered by pk
print(AccountsUserProxy.objects.all())  # ordered by 'first_name'
