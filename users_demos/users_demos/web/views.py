from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins


def index(request):
    print(request.user)
    return HttpResponse("It works!")


""" 
LOGIN REQUIRED TO ACCESS A PAGE WITH FBV 
--->
    from django.contrib.auth.decorators import login_required
    
When the user is not logged in, it will show us login page, 
and once it's logged in, it will redirect to 'about' page. 
Because we have added the redirect login URL to 'login-user' page in settings.py:

    # IF next is provided:  (means we try to reach 'about' or 'team' page but both of them are login required pages)
    LOGIN_URL = reverse_lazy("login-user")
    
    # If next is not provided:  (means that we directly try to reach login page)
    LOGIN_REDIRECT_URL = reverse_lazy("index")
"""


@login_required  # Checks if the user is authenticated. We add it to show 'about' view only on logged in users
def about(request):
    return HttpResponse(f"It's about that, {request.user}!")


""" 
LOGIN REQUIRED TO ACCESS A PAGE WITH CBV 
--->
    from django.views import generic as views
    from django.contrib.auth import mixins as auth_mixins
    
When the user is not logged in, it will show us login page, 
and once it's logged in, it will redirect to 'team' page.
Because we have added the redirect login URL to 'login-user' page in settings.py:

    # IF next is provided:  (means we try to reach 'about' or 'team' page but both of them are login required pages)
    LOGIN_URL = reverse_lazy("login-user")
    
    # If next is not provided:  (means that we directly try to reach login page)
    LOGIN_REDIRECT_URL = reverse_lazy("index")
"""


class TeamView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f"{request.user}'s team!")
