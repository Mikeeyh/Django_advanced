from django.http import HttpResponse
from django.urls import path

urlpatterns = (
    path("", lambda r: HttpResponse("It works"), name="index"),
)