from random import randint
Number_of_sticks = int(input('Количество палок: '))
Number_of_throws = int(input('Количество бросков: '))

list_of_sticks = ['|'] * Number_of_sticks

for i in range(Number_of_throws):
    Left_i = randint(1, Number_of_sticks)
    Right_i = randint(Left_i, Number_of_sticks)
    list_of_sticks[Left_i:Right_i] = ['.' for _ in range(Left_i, Right_i + 1)]
    print(f'Бросок {i}. Сбиты палки с номера {Left_i} по номер {Right_i}.')
print("".join(list_of_sticks))