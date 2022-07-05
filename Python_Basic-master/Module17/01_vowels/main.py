mylist = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
txt = input('Введите текст: ').lower()
outputlist = [i for i in txt if i in mylist]
print('Список гласных букв:', outputlist)
print('Длина списка: ', len(outputlist))