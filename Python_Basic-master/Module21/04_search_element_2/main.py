site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(structure, key, count=None):
    if count is None:
        if key in structure.keys():
            return structure[key]
        else:
            for i in structure.values():
                if isinstance(i, dict):
                    val = find_key(i, key)
                    if val:
                        return val
            else:
                return None
    else:
        if count <= 0:
            return None
        if key in structure.keys():
            return structure[key]
        else:
            for i in structure.values():
                if isinstance(i, dict):
                    val = find_key(i, key, count=count - 1)
                    if val:
                        return val
            else:
                return None


search_key = input('Введите искомый ключ:')
choice = input('Хотите ввести максимальную глубину? Y/N:').lower()

if choice == 'n':
    print('Значение ключа:', find_key(site, search_key))
elif choice == 'y':
    max_iter = int(input('Введите максимальную глубину: '))
    print('Значение ключа:', find_key(site, search_key, count=max_iter))
