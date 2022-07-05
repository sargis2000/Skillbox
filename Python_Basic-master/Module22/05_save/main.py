import os


def editor():
    text = input('Введите строку: ')
    where_to_save = os.path.join(
        os.path.expanduser('~'),
        input('Куда хотите сохранить документ? '
              'Введите последовательность папок (через пробел):\n').replace(' ', '/')
    )

    if os.path.exists(where_to_save):
        name_file = input('Введите имя файла:') + '.txt'
        file_path = os.path.join(
            where_to_save,
            name_file
        )
        if os.path.exists(file_path) and os.stat(file_path).st_size != 0:
            if input('Вы действительно хотите перезаписать файл?').lower() == 'да':
                open(file_path, 'w').write(text)
                print('Файл успешно перезаписан!')
                with open(file_path, 'r') as file:
                    for i in file:
                        print(i, end=' ')
                    file.close()
            else:
                print('Canceled!!')
        else:
            open(file_path, 'w').write(text)
            print('Файл успешно сохранён!')
            print('Содержимое файла:\n')
            with open(file_path, 'r') as file:
                for i in file:
                    print(i, end=' ')
                file.close()

    else:
        print('enter correct path Invalid Path:', where_to_save)
        editor()

editor()
