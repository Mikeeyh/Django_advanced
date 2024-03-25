import time

from django.utils.deprecation import MiddlewareMixin

""" Template for middlewares """


# 'get_response' is a function

# def measure_time(get_response):
#     def middleware(request, *args, **kwargs):
#
#         pass
#         result = get_response(request, *args, **kwargs)
#         pass
#
#         return result
#
#     return middleware


""" Using class """


class MeasureExecutionTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):  # Before the request:
        self.start_time = time.time()

    def process_response(self, request, response):  # After the request:
        self.end_time = time.time()
        print(f"{request.method} {request.path} executed in {self.end_time - self.start_time} seconds")
        return response


""" Using method """


def measure_time(get_response):
    def middleware(request, *args, **kwargs):

        # Before the request:
        start_time = time.time()

        result = get_response(request, *args, **kwargs)

        # After the request:
        end_time = time.time()
        print(f"{request.method} {request.path} executed in {end_time - start_time} seconds")

        return result

    return middleware
