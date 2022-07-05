summa = 0
try:
    with open('calc.txt', 'r') as read_file:
        for line in read_file:
            try:
                summa += eval(line)
            except SyntaxError:
                choice = input(f'Обнаружена ошибка в строке: {line.rstrip()}   Хотите исправить?')
                while True:
                    if choice.lower() == 'да':
                        summa += eval(input('Введите исправленную строку:'))
                        break
                    elif choice.lower() == 'нет':
                        break

except FileNotFoundError:
    print('Create calc.txt file')
else:
    print(summa)
