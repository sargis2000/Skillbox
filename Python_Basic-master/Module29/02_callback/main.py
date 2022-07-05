from functools import wraps
from typing import Callable
app = {}


def callback(route: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        app[route] = func

        @wraps(func)
        def wrapped() -> Callable:
            ret = func()
            return ret
        return wrapped
    return wrapper


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')