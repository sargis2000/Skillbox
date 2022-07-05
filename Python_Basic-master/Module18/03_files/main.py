special_symbols = list('@№$%^&*().')
ending = ['.txt', '.docx']

file_name = input('Название файла: ')
if file_name.endswith(ending[0]) or file_name.endswith(ending[1]):
    for i in special_symbols:
        if file_name.startswith(i):
            print('Ошибка: название начинается на один из специальных символов.')
            break
    else:
        print('Файл назван верно.')

else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
