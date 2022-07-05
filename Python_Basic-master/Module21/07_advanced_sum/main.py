list_for_sum = [[1, 2, [3]], [1], 3, [10, 8, [95, 10]]]
summ = 0


def my_own_sum(*obj):
    global summ
    if isinstance(obj[0], list):
        for i in obj[0]:
            if isinstance(i, list):
                obj = my_own_sum(i)
            else:
                summ += i
    else:
        for i in obj:
            summ += i
    return summ


print(my_own_sum(list_for_sum))

