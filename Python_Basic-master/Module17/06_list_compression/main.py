from random import randint
count = int(input('Количество чисел в списке: '))
list_of_num = [randint(0, 2) for _ in range(count)]
print(list_of_num)
list_of_num = [i for i in list_of_num if i != 0]
print(list_of_num)
