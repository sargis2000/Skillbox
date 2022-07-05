text = input('Введите строку: ')
print('Закодированная строка: ', end='')
cont = 1
for i in range(len(text)):
    if i != len(text) - 1:
        if text[i] == text[i + 1]:
            cont += 1
        else:
            print(''.join([text[i], str(cont)]), end='')
            cont = 1
    else:
        if text[i] == text[i - 1]:
            cont += 1
        else:
            print(''.join([text[i], str(cont)]), end='')
            cont = 1

