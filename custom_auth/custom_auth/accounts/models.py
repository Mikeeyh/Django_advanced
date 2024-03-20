from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone

from django.apps import apps
from django.contrib import auth
from django.contrib.auth import base_user as auth_base
from django.contrib.auth import get_user_model, models as auth_models

"""
1. Use the default user as-is
2. Extend the default user and add more stuff (Extend the 'AbstractUser' class)
3. Rewrite the whole user (Extend the 'AbstractBaseUser' class)
"""

"""
TWO WAYS TO EXTEND THE USER MODEL:
"""

"""
1. Extend the built-in user model through 'AbstractUser':
    - Add 'age' field.
    - Add 'gender' field.

# Better at:
    - Simpler
    - No need to rewrite Django auth system
    
We just need to:
    add AUTH_USER_MODEL = 'accounts.AccountUser' in settings.py
    create new custom form 'AccountUserCreationForm' in views.py or forms.py
    add the form in register view 'form_class = AccountUserCreationForm' in views.py
    
    And for administration, to see users:
        @admin.register(UserModel)
        class UserModelAdmin(admin.ModelAdmin):
            pass

"""

# UserModel = get_user_model()


# class AccountUser(auth_models.AbstractUser):
#     age = models.PositiveIntegerField(
#         blank=True,
#         null=True,
#     )


"""
2. Extend the user through a One-to-One relationship with 'Profile' model:
    - Add 'age' field.
    - Add 'gender' field.

2.1 Use the built-in user for auth

# Better at:
    - Easier migration to other auth model in the future
    - No need to rewrite Django auth system
"""

# UserModel = get_user_model()
#
#
# class Profile(models.Model):
#     age = models.PositiveIntegerField(
#         blank=False,
#         null=False,
#     )
#
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.DO_NOTHING,
#         primary_key=True,
#     )

"""
2. Extend the user through a One-to-One relationship with 'Profile' model:
    - Add 'age' field.
    - Add 'gender' field.

2.2 Create our own user model

# Better at:
    - Easier migration to other auth model in the future
    - No need to rewrite Django auth system
"""


class AccountUserManager(auth_base.BaseUserManager):  # We have 'get_by_natural_key error' so we add this line
    use_in_migrations = True

    # Adding those 4 functions from AbstractUser -> UserManager() in order to be able to create superusers&users.
    # We just removed 'username' from the functions and/or replaced it with 'email' because we are using email for login
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class AccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):  # Auth DATA
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active."
            "Unselect this instead of deleting accounts."
        ),  # if we have is_active error we add this line too
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    ) # Adding is_staff because we cannot access the administration (/admin) without this

    # This is the other (username) part of the **credentials**
    USERNAME_FIELD = "email"

    objects = AccountUserManager()


class Profile(models.Model):  # User DATA
    age = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    user = models.OneToOneField(
        AccountUser,  # here we do not need to call 'UserModel' because 'AccountUser' is just above
        on_delete=models.DO_NOTHING,
        primary_key=True,
        related_name="profile",
    )


# class AccountsUserProxy(UserModel):
#     # age = models.IntegerField()  # will not work
#
#     class Meta:
#         proxy = True
#         ordering = ('first_name',)
#
#     def some_custom_behavior(self): ...
#
#
# print(UserModel.objects.all())  # ordered by pk
# print(AccountsUserProxy.objects.all())  # ordered by 'first_name'
