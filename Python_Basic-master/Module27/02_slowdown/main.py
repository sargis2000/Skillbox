from typing import Callable, Any
from functools import wraps
from time import sleep


def sleeper(func: Callable) -> Callable:
    @wraps(func)
    def wrapping(*args: Any, **kwargs: Any) -> Callable:
        sleep(3)
        res = func()
        return res
    return wrapping


@sleeper
def printer() -> None:
    print("lol")

printer()


