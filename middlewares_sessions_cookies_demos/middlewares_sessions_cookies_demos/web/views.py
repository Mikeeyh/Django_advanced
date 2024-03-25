import time
from time import sleep

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views


# class ExecuteBeforeRequest:
#     def dispatch(self, request, *args, **kwargs):
#
#         # Code before the request
#
#         dispatch_result = super().dispatch(request, *args, **kwargs)
#
#         # Code after the result
#
#         return dispatch_result


class MeasureExecutionTimeMixin:
    def dispatch(self, request, *args, **kwargs):

        start_time = time.time()

        dispatch_result = super().dispatch(request, *args, **kwargs)

        end_time = time.time()
        print(f"Executed in {end_time - start_time} seconds")

        return dispatch_result


def get_load_count(request):
    load_count = request.session.get('load_count', 0)

    return load_count + 1


# class IndexView(MeasureExecutionTimeMixin, views.TemplateView):
#     template_name = 'web/index.html'
#
#     def get_context_data(self, **kwargs):  # overwriting to add 'sleep'
#
#         sleep(1)
#
#         context = super().get_context_data(**kwargs)
#
#         load_count = get_load_count(self.request)
#         self.request.session['load_count'] = load_count
#         context['load_count'] = load_count
#
#         return context


""" It is not very good to have this logic in get_context_data method, so it is better to move it in dispatch method """


class IndexView(MeasureExecutionTimeMixin, views.TemplateView):
    template_name = 'web/index.html'

    def dispatch(self, request, *args, **kwargs):
        load_count = get_load_count(request)
        request.session['load_count'] = load_count
        print(request.COOKIES)

        response = super().dispatch(request, *args, **kwargs)

        response.set_cookie('load_count', load_count)
        
        return response

    def get_context_data(self, **kwargs):  # overwriting to add 'sleep'

        sleep(1)

        context = super().get_context_data(**kwargs)
        context['load_count'] = self.request.session.get('load_count', 0)

        return context

