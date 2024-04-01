from django.contrib.auth import get_user_model
from rest_framework import generics as api_views, serializers, permissions
from rest_framework.authtoken import views as api_token_views

UserModel = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):  # For 'CreateUserApiView'
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def to_representation(self, *args, **kwargs):  # Overwriting this method to hide the password.
        representation = super().to_representation(*args, **kwargs)
        representation.pop('password', None)

        # When we click on 'CreateAPIView' we see that we return 'self.create'
        # When we click on 'create' we see that we return 'serializer.data'
        # We found 'to_representation' from 'serializers' -> 'save' method.

        return representation


class CreateUserApiView(api_views.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = UserModel.objects.all()

    permission_classes = [permissions.AllowAny]


"""
ERROR: TemplateDoesNotExist at /api/auth/create/ -> rest_framework/api.html

Solution: 
1. Settings.py -> INSTALLED_APPS -> Add -> 'rest_framework'
"""


class LoginApiView(api_token_views.ObtainAuthToken):
    permission_classes = [permissions.AllowAny]


class LogoutApiView:
    permission_classes = [permissions.IsAuthenticated]
