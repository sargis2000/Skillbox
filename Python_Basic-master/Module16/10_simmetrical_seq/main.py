def ispalindrom(mystr):
    if mystr != mystr[:: -1]:
        return False
    else:
        return True


numbers_count = int(input('Кол-во чисел:'))
mylist = []
isertion_list = []
for i in range(numbers_count):
    mylist.append(int(input('Число: ')))
print('Последовательность:', mylist)

mylist.append(mylist[0])
isertion_list.append(mylist[0])
listToStr = ' '.join(map(str, mylist))
if ispalindrom(listToStr):
    pass
else:
    for i in mylist[1:]:
        listToStr = ' '.join(map(str, mylist))
        if ispalindrom(listToStr):
            break
        else:
            mylist.insert(-mylist.index(i), i)
            isertion_list.append(i)
print('Нужно приписать чисел:', len(isertion_list))
print('Сами числа:', isertion_list[:: -1] )



