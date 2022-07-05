from random import randint

max_number = int(input('Введите максимальное число: '))
Artem_number = randint(0, max_number)
values = set(n for n in range(max_number))
while True:
    numbers = input('Нужное число есть среди вот этих чисел: ')
    if numbers == 'Помогите!':
        break
    else:
        numbers = set(int(n) for n in numbers.split())
        if Artem_number in numbers:
            values = values & numbers
            print('Ответ Артёма: YES')
        else:
            print('Ответ Артёма: NO')
            values -= numbers


print('Артём мог загадать следующие числа:', values)

