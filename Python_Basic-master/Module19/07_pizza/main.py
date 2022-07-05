iter_counts = int(input('Введите количество заказов: '))
order_dict = dict()
for i in range(1, iter_counts + 1):
    order = input('Первый заказ:').split()
    if order[0] not in order_dict.keys():
        order_dict[order[0]] = {order[1]: order[2]}
    else:
        order_dict[order[0]][order[1]] = order[2]


for i in order_dict.keys():
    print(i, ":")
    for pizza, count in order_dict[i].items():
        print(f'\t{pizza} : {count}')

