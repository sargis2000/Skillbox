from random import choice
errors = (ZeroDivisionError, FileNotFoundError, AssertionError,
          NotADirectoryError, IndexError, ValueError, FileNotFoundError, BlockingIOError,
          MemoryError, ModuleNotFoundError)
summa = 777
with open('out_file.txt', 'w') as file:
    while summa >= 0:
        number = input('Введите число: ')
        try:
            number = int(number)
        except ValueError:
            print("I'm not stupid  program !!!!\nEnter  just numbers")
        else:
            summa -= number
            if choice(range(0, 13)) == 7:
                raise choice(errors)('Вас постигла неудача!')
            else:
                file.write(str(number) + '\n')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')