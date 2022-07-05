# configure python interpriter
# activate venv
# run this command --------------------------> pip install sympy
# or set up manual
# !!!!  Is there way   to set my own script  in pip?    !!!!!!!!!!!!
from sympy import isprime
from math import sqrt


def smol_divisor(n):
    if n == 0 or n == 1:
        return 'Do not have divisor small then 1'
    elif isprime(n):
        return n
    elif n % 2 == 0:
        return 2
    else:
        for i in range(3, int(sqrt(n)), 2):
            if n % i == 0:
                return i


def main():
    number = int(input("Enter the number "))
    print('Наименьший делитель, отличный от единицы:',smol_divisor(number))


main()
