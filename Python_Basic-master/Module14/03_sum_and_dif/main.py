def summator(n):
    summ = 0
    for i in n:
        summ += int(i)
    return summ


def main():
    number = input("Введите число: ")
    if number.isdigit():
        sum_num = summator(number)
        length = len(number)
        print('Сумма чисел: ', sum_num)
        print('Количество цифр в числе:', length)
        print('Разность суммы и количества цифр:', sum_num - length)
    else:
        main()


main()
