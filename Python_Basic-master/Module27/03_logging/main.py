from typing import Callable, Any
from datetime import datetime
import functools


def dec_loging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        try:
            res = func(*args, *kwargs)
            print('Function name---------->', func.__name__)
            print('Func Docs:', func.__doc__)
            return res
        except Exception as e:
            with open('function_errors.log', 'a+') as file:
                file.write('Function name: {name}:\nError: {error} :\nTime:{curr_time}\n'.format(
                    name=func.__name__,
                    error=e,
                    curr_time=datetime.now()
                ))
    return wrapper


@dec_loging
def lol(arg1: int) -> int:
    """
    Any Doc Here
    :param arg1:
    :return: None
    """
    return arg1 + 2


x = lol()
lol(10)
lol('aaa')



