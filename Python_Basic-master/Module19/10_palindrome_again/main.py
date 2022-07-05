text = input('Введите строку: ')
mydict = dict()
for i in text:
    count = text.count(i)
    if count % 2 != 0:
        mydict[i] = mydict.get(i, True)
if len(mydict) > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')