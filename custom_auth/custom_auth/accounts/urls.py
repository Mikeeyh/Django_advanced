from django.urls import path

from custom_auth.accounts.views import LoginUserView, RegisterUserView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("register/", RegisterUserView.as_view(), name="register_user"),
)

# We remove 'RegisterUserView' and the path of it in order to make migrations of 2.2 way to extend the 'User' model,
# Then we revert it back
