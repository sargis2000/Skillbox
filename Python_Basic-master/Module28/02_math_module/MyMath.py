from abc import ABC


class MathFuncs(ABC):
    from typing import Union
    from math import pi

    @classmethod
    def circle_len(cls, radius: Union[int, float]) -> Union[int, float]:
        return 2 * cls.pi * radius

    @classmethod
    def circle_sq(cls, radius: Union[int, float]) -> Union[int, float]:
        return radius ** 2 * cls.pi

    @classmethod
    def cube_volume(cls, edge: Union[int, float]) -> Union[int, float]:
        return edge ** 3

    @classmethod
    def sphere_surface_area(cls, radius: Union[int, float]) -> Union[int, float]:
        return radius ** 2 * cls.pi * 4


