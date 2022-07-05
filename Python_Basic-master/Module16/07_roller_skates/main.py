item_count = int(input('Кол-во коньков: '))
item_list = []
count = 0
for i in range(item_count):
    item_list.append(int(input(f'Размер {i + 1}-й пары:')))


men_count = int(input('Кол-во людей: '))
for i in range(men_count):
    size_leg = int(input('Размер ноги 1-го человека:'))
    if size_leg in item_list:
        count += 1
        item_list.remove(size_leg)
print('Наибольшее кол-во людей, которые могут взять ролики:', count)