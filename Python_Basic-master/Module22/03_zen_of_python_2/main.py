import os
from string import ascii_uppercase


def myfunc(file, mode):
    chars_dict = dict()
    for line in file:
        line = line.upper()
        for i in ascii_uppercase:
            item = chars_dict.get(i, False)
            if not item:
                chars_dict[i] = line.count(i)
            else:
                chars_dict[i] = item + line.count(i)
    chars_dict = {key: val for key, val in chars_dict.items() if val != 0}
    minimum = min(chars_dict.values())
    if mode == 'min_val':
        return tuple(key for key, val in chars_dict.items() if val == minimum)
    elif mode == 'sum':
        return sum(chars_dict.values())
    else:
        return 'Enter correct mode'


def word_line_counter(file, mode):
    word_count, line_count = 0, 0
    for line in file:
        line_count += 1
        word_count += len(line.split())
    if mode == 'word':
        return word_count
    elif mode == 'line':
        return line_count
    else:
        return 'Enter correct mode'


with open(os.path.join('..', '02_zen_of_python', 'zen.txt'), 'r') as zen:
    print('Количество букв в файле:', myfunc(zen, 'sum'))
    zen.seek(0)
    print('Наиболее редкая буква:', myfunc(zen, 'min_val'))
    # Я печатаю tuple(), потому что может быть  более одного минимального значения
    zen.seek(0)
    print('Количество слов в файле:', word_line_counter(zen, 'word'))
    zen.seek(0)
    print('Количество строк в файле:', word_line_counter(zen, 'line'))
    zen.close()

