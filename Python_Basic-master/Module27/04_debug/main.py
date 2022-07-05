from typing import Callable, Any
import functools


def dec(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        arguments = '('
        for i in args:
            arguments += i + ', '
        for i in kwargs:
            arguments += f'{i}={kwargs[i]}, '
        arguments += ')'

        print("Вызывается {name}{args}".format(
            name=func.__name__,
            args=arguments,
        ))
        res = func(*args, **kwargs)
        print(f"{func.__name__} вернула значение {res}")
        print(res)
        return res
    return wrapper


@dec
def greeting(name: str, age: int = None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
