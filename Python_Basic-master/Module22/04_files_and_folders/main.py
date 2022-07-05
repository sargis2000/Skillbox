import os


def dir_size(path):
    size = 0
    if os.path.isdir(path):
        for i in os.listdir(path):
            new_path = os.path.join(path, i)
            size += dir_size(new_path)
    elif os.path.isfile(path):
        return os.path.getsize(path) / 1024
    else:
        print('Something wrong with this', path)
    print(path, size, 'kb')
    return size


def dir_info():
    path = input('Enter the path')
    try:
        x = os.listdir(path)
    except FileNotFoundError:
        print('Enter correct path')
        dir_info()
    else:
        count_dir, count_file, size = 0, 0, 0
        for i in x:
            new_path = os.path.join(path, i)
            if os.path.isdir(new_path):
                size += dir_size(new_path)
                count_dir += 1
            elif os.path.isfile(new_path):
                print(new_path, size)
                size += round(os.path.getsize(new_path) / 1024, 10)
                count_file += 1
            else:
                print('Something wrong with this we cant find or cant get size', new_path)
        return count_dir, count_file, size


information = dir_info()
print(information)
print(
    'Количество подкаталогов: ', information[0],
    '\nКоличество файлов: ', information[1],
    '\nРазмер каталога (в Кб): ', information[2]
)


