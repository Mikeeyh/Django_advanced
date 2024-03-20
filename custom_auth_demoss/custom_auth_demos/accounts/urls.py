from django.urls import path

from custom_auth_demos.accounts.views import LoginUserView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login_user"),
)
