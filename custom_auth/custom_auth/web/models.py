from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Model1(AuditModel, models.Model):
    field = models.CharField(max_length=20)

    # Do THIS: (this is for our 1. way to create custom user)
    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.DO_NOTHING,
    # )
    # Example: request.user.model1_set()

    # DO NOT DO THIS:
    # profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.DO_NOTHING,
    # )
    # Example: request.user.profile.model1_set()
    # Explanation: If we want to access a user's 'model1' from 'profile' we should make the request above.
    # The only role of the 'profile' is to store personal stuff
