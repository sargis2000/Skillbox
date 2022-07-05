text = input('Введите текст: ')


def diction(txt):
    print('Оригинальный словарь частот:')
    dictionary = dict()
    for i in txt:
        if i not in dictionary.keys():
            dictionary[i] = txt.count(i)
    for i in dictionary.keys():
        print(i, ':',dictionary[i])
    return dictionary


def list_print(mydict):
    for i in set(mydict.values()):
        list_of_keys = list()
        for j in mydict.keys():
            if mydict[j] == i:
                list_of_keys.append(j)
        print(i, ":", list_of_keys)


list_print(diction(text))
