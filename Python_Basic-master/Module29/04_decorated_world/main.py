from typing import Callable
from functools import wraps


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:

    def decorator_maker(*args, **kwargs):
        @wraps(decorator)
        def decorator_wrapper(func):
            print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
            return func
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    return func(args, kwargs)


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)