list1, list2 = [], []
for i in range(3):
    list1.append(int(input(f'Введите {i + 1}-е число для первого списка:')))
for i in range(7):
    list2.append(int(input(f'Введите {i + 1}-е число для второго списка:')))
print('Первый список:', list1)
print('Второй список:', list2)
list1.extend(list2)
list1 = list(dict.fromkeys(list1))
print('Новый первый список с уникальными элементами:', list1)

