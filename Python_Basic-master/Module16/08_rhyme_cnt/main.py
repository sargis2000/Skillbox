menlist = list(range(1, int(input('Кол-во человек: ')) + 1))
number = int(input('Какое число в считалке?'))
print(f'Значит, выбывает каждый {number}-й человек')
start_index = 0


def chicker(mylist, index):
    print('Выбывает человек под номером', mylist[start_index - 1])
    mylist.pop(index)
    mylist = mylist[index:] + mylist[:index]
    return mylist


while len(menlist) > 1:
    print('--------------------------------------------------------------------')
    print('Текущий круг людей:', sorted(menlist))
    print('Начало счёта с номера ', menlist[0])

    start_index = number % len(menlist)
    menlist = chicker(menlist, start_index - 1)

print('Остался человек под номером', menlist[0])