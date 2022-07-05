import re
phone_list = ['9999999999', '999999-999', '99999x9999']

for i in phone_list:
    if re.match(r'[89]\d{9}', i):
        print('всё в порядке c ', i)
    else:
        print(i, 'номер: не подходит')