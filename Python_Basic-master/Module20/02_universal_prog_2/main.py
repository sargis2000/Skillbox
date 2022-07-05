from sympy import isprime


def crypto(obj):
    return [j for i, j in enumerate(obj) if isprime(i)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

