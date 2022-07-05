import math
from typing import NoReturn, Any, Union
from abc import ABC, abstractmethod


class Model2D(ABC):
    @classmethod
    def checker(cls, val: Any) -> float:
        while True:
            try:
                val = float(val)
                return val
            except TypeError:
                val = input('Pls Try again')


class Triangle(Model2D):

    def __init__(self) -> NoReturn:
        self._base = self.checker(input('Enter  Triangle base'))
        self._height = self.checker(input('Enter  Triangle Height'))

    def perimeter(self) -> Union[int, float]:
        return 2 * math.sqrt((self._base / 2) ** 2 + self._height ** 2) + self._base

    def seq(self) -> Union[int, float]:
        return self._base * self._height / 2

    @property
    def base(self) -> Union[int, float]:
        return self._base

    @property
    def height(self) -> Union[int, float]:
        return self._height

    @height.setter
    def height(self, val: Union[int, float]):
        self._height = val

    @base.setter
    def base(self, val: Union[int, float]):
        self._base = val


class Square(Model2D):

    def __init__(self) -> NoReturn:
        self._leg1 = self.checker(input('Enter Square leg'))

    def perimeter(self) -> Union[int, float]:
        return 4 * self._leg1

    def seq(self) -> Union[int, float]:
        return self._leg1 ** 2

    @property
    def leg1(self):
        return self._leg1

    @leg1.setter
    def leg1(self, val):
        self._leg1 = val


class Pyramid:
    def __init__(self):
        print('Pyramid can be crated using  4 tryangle and  1 square')

    @classmethod
    def surface_are(cls) -> Union[int, float]:
        return 4 * Triangle().seq() + Square().seq()


class Cube:
    def __init__(self):
        print('Cube can be crated using 6 square')

    @classmethod
    def surface_are(cls) -> Union[int, float]:
        return 6 * Square().seq()


print(Cube().surface_are())
print(Pyramid().surface_are())
