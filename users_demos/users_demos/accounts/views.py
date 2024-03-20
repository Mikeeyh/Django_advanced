from django.views import generic as views
from django.urls import reverse, reverse_lazy

from django.contrib.auth import views as auth_views, get_user_model, forms as auth_forms

from users_demos.accounts.forms import CreateUserForm

# 'authenticate(request, **credentials)' -> returns the user if credentials match
# 'login(request, user) -> attaches a cookie for the authenticated user

# Correct way to get the 'User' class:
UserModel = get_user_model()


class LoginUserView(auth_views.LoginView):  # login view from django:
    template_name = "accounts/login_user.html"


class RegisterUserView(views.CreateView):
    # form_class = auth_forms.UserCreationForm  # We have this 'UserCreationForm' from Django
    form_class = CreateUserForm  # Using our custom form from forms.py
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy("index")


# Writing our own login view:
# class LoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class(),
#         }
#
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # form = self.form_class(request.POST or None)
#         # if form.is_valid():
#
#         username, password = request.POST["username"], request.POST["password"]
#
#         user = authenticate(username=username, password=password)
#         print(user)
#
#         if user is not None:
#             # Add the user to the session
#             login(request, user)
#         return redirect("index")
