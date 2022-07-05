iter_count = int(input('Сколько записей вносится в протокол? '))
win_dict = {
    '1-е место': (0, "noname"),

    '2-е место': (0, "noname"),

    '3-е место': (0, "noname"),
}
for i in range(iter_count):
    rec = input(f'{i + 1}-я запись: ').split()
    if int(rec[0]) > win_dict['1-е место'][0]:
        win_dict['2-е место'] = win_dict['1-е место']
        win_dict['1-е место'] = (int(rec[0]), rec[1])
    elif int(rec[0]) > win_dict['2-е место'][0]:
        win_dict['3-е место'] = win_dict['2-е место']
        win_dict['2-е место'] = (int(rec[0]), rec[1])
    elif int(rec[0]) > win_dict['3-е место'][0]:
        win_dict['3-е место'] = (int(rec[0]), rec[1])
    else:
        continue

for i, j in win_dict.items():
    print(f'{i}.{j[1]} {j[0]}')