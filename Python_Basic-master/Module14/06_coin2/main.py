def main():
    x1 = float(input('Введите координаты монетки:\nX:'))
    x2 = float(input('Y: '))
    radius = float(input('Enter the radius: '))
    check = checker(x1, x2, radius)
    if check:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


def checker(x1, x2, r):
    if x1 ** 2 + x2 ** 2 <= r:
        return True
    else:
        return False


main()
