a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
cont_5 = a.count(5)
print('Кол-во цифр 5 при первом объединении:', cont_5)
for i in range(cont_5):
    a.remove(5)
a.extend(c)
print('Кол-во цифр 3 при втором объединении:', a.count(3))
print('Итоговый список:', a)


