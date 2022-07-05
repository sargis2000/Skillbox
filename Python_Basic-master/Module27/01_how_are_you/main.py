import functools
from collections.abc import Callable
from typing import Any


def my_dec(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        input('Hi How ate you')
        print('А у меня не очень! Ладно, держи свою функцию.\nHere your function!!!!!!!!!!!')
        res = func()
        return res
    return wrapper


@my_dec
def printer() -> None:
    print('LOL!!!!')


printer()
