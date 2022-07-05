def add_contact(contacts):
    contact = tuple(input('Введите имя и фамилию нового контакта (через пробел):').title().split())
    if contact not in contacts.keys():
        number = input('Введите номер телефона: ')
        contacts[contact] = number
        print(f'Текущий словарь контактов:{contacts}')
        main()
    else:
        print('Такой человек уже есть в контактах.')
        print(f'Текущий словарь контактов:{contacts}')
        main()


def search(contacts):
    contact = input('Введите фамилию для поиска:').capitalize()
    for i, j in contacts.keys():
        if i == contact or j == contacts:
            print(f'{i} {j} {contacts[(i, j)]}')
    main()


def main():
    choice = int(input('\nВведите номер действия:\n1. Добавить контакт\n2. Найти человека\n'))
    if choice == 1:
        add_contact(contacts)
    elif choice == 2:
        search(contacts)
    else:
        print('Enter corrrect choice')
        main()


if __name__ == '__main__':
    contacts = dict()
    main()
