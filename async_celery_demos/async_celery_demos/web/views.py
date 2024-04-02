import time

from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def index(request):
    user_count = UserModel.objects.count()
    title = "It works!"

    context = {
        "title": title,
        "user_count": user_count,
    }

    print("Timer started")
    time.sleep(10)
    print("Timer ended")

    return render(request, "...", context)
