chars_count = 0
iter_count = 0
try:
    with open('people.txt', 'r') as file:
        with open('error.log', 'w') as error_file:
            for i in file:
                try:
                    iter_count += 1
                    if len(i) >= 4:
                        chars_count += len(i) - 1
                    else:
                        raise IndexError
                except IndexError:
                    error = f'Ошибка: менее трёх символов в строке {iter_count}'
                    error_file.write(error + '\n')
                    print(error)
except FileNotFoundError:
    print('Ctreate people.txt File!!!!')
else:
    print('Общее количество символов: ', chars_count)


