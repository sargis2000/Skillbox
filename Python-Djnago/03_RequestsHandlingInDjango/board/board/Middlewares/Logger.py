from typing import Callable
from datetime import datetime


def midd_decorator(get_response: Callable) -> Callable:
    def middleware_wrapper(request):
        with open('request_loger.log', 'a+') as file:
            file.write('request time "{date}"   request path"{request_path}" and request method "{method}"\n'.format(
                request_path=request.path,
                date=datetime.now(),
                method=request.method
            ))
        response = get_response(request)

        return response
    return middleware_wrapper

