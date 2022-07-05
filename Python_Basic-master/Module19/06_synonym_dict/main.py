iter_count = int(input('Введите количество пар слов: '))
dictionary = dict()
for i in range(1, iter_count + 1):
    item = input(f'{i} пара:').lower().split('-')
    dictionary[item[0]] = item[1]

print(dictionary)
for i in range(1, iter_count + 1):
    word = input('Введите слово: ').lower()
    if word in dictionary.keys():
        print(f'Синоним:{dictionary[word]}')
    elif word in dictionary.values():
        for j in dictionary.keys():
            if dictionary[j] == word:
                print(f'Синоним:{j}')
    else:
        print('Такого слова в словаре нет.')