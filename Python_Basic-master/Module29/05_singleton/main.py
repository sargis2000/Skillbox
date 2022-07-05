from typing import Callable
from functools import wraps


def singleton(obj: Callable) -> Callable:
    inst = {}

    @wraps(obj)
    def wrapper(*args, **kwarg):
        inst[obj] = obj
        if obj not in inst:
            return obj
        return inst[obj]
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))


print(my_obj is my_another_obj)




