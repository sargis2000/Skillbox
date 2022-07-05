from collections.abc import Iterable
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def finder(to: int) -> Iterable:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to:
                yield True
            yield False


a = finder(to=to_find)
for i in a:
    if i:
        print('Found!!!')
        break


