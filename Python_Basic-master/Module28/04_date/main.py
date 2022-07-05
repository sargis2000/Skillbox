# pip install python-dateutil
import math
from abc import ABC
from dateutil.parser import parse


class Date(ABC):
    @classmethod
    def is_date_valid(cls, val: str) -> bool:
        try:
            parse(val)
            return True
        except Exception:
            return False

    @classmethod
    def from_string(cls, val: str) -> str:
        if cls.is_date_valid(val):
            val = val.split('-')
            return f'День: {val[0]}    Месяц: {val[1]}    Год: {val[2]}'
        else:
            print("ARTEM!!!!!  I'm not stupid program ")


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

