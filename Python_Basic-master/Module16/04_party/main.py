guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:{guests}')
    choice = input('Гость пришёл или ушёл?')
    if choice == 'пришёл':
        name_guest = input('Имя гостя:')
        if len(guests) <= 5:
            guests.append(name_guest)
            print('Привет,', name_guest, '!')
        else:
            print(f'Прости, {name_guest}, но мест нет.')
    elif choice == 'ушёл':
        name_guest = input('Имя гостя:')
        guests.remove(name_guest)
        print(f'Пока, {name_guest}!')
    elif choice == 'Пора спать':
        print('Вечеринка закончилась, все легли спать')
        break
    else:
        print('Enter correct choice')