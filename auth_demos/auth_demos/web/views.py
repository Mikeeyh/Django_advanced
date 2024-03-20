from django.http import HttpResponse
from django.shortcuts import render

from auth_demos.web.models import Model1


def index(request):
    param = "1"  # From request

    # # No possible SQL injection
    # model1_list = list(Model1.objects.all() \
    #                    .filter(pk=param))

    # # Possible SQL injection
    # model1_list2 = list(Model1.objects.raw(f'SELECT * FROM web_model1 WHERE id={param}'))
    #
    # # NOT Possible SQL injection
    # model1_list3 = list(Model1.objects.raw(f'SELECT * FROM web_model1 WHERE id={param}', params={'id': param}))

    context = {
        'model1_list': Model1.objects.all(),
    }
    return render(request, "index.html", context)


def private_view(request):
    return HttpResponse("View Accessed")
