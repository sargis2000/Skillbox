dict_of_countries = dict()
iter_count = int(input('Количество стран: '))
for i in range(iter_count):
    country = input(f'страна {i + 1}:').split()
    dict_of_countries[country[0]] = country[1:]
for i in range(3):
    check = input(f'город {i + 1}: ')
    for val in dict_of_countries:
        if check in dict_of_countries[val]:
            print(f'Город {check} расположен в стране {val}.')
            break
    else:
        print(f'По городу {check} данных нет.')
