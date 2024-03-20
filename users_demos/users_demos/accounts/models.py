from django.db import models

# Just add new fields:
# class AppUser(AbstractUser):
#     age = models.PositiveIntegerField()

# Completely replace the User:
# class AppUser(AbstractBaseUser():
#    USERNAME_FIELD = "email"  # we can change the variable
#    pass

# getattr(self, "email")

# AnonymousUser =