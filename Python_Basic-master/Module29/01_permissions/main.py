from functools import wraps
from typing import Callable


def check_permission(perm: str):
    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if perm not in user_permissions:
                raise PermissionError(' У {} недостаточно прав, чтобы выполнить функцию {}'.format(
                    perm, func.__name__
                ))
            return func()
        return wrapper
    return inner


user_permissions = ['admin', 'Sargis']


@check_permission('Sargis')
def delete_site():
    print('Удаляем сайт')


@check_permission('admin')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()