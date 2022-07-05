import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        with open('result.txt', 'w') as file_2:
            for line in file:
                nums_list = line.split()
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(my_list))
except FileNotFoundError:
    print("We ant finde file")
