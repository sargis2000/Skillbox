iter_count = int(input('Введите количество человек: '))
mydict = dict()
mydict['Peter_I'] = 0
for i in range(1, iter_count):
    name = input(f'пара {i}:').split()
    if name[0] not in mydict.keys():
        mydict[name[0]] = mydict[name[1]] + 1

print('«Высота» каждого члена семьи:')
for i, j in mydict.items():
    print(i, j)



