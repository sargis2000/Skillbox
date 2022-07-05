max_val = int(input('Enter number!'))


def printer(num):
    if num == 1:
        return 1
    print(num)
    return printer(num - 1)


def printer2(num, start=1):
    if num == start:
        return num
    print(start)
    return printer2(num, start + 1)


# print(printer(max_val))
print(printer2(max_val,))
