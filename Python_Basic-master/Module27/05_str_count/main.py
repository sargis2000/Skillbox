import functools
from typing import Callable


def my_counter(func: Callable) -> Callable:
    class Counter:
        def __init__(self):
            self.count = 0

        def plus(self):
            self.count += 1
            print('Call count = ', self.count)

    a = Counter()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        a.plus()
        res = func()
        return res

    return wrapper


@my_counter
def lol():
    print('Calleed Func 1')


@my_counter
def ankap():
    print('Called Func 2')


lol()
lol()
ankap()
ankap()
ankap()
ankap()
ankap()
lol()


