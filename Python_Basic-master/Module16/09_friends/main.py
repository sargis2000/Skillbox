friends_count = int(input('Кол-во друзей:'))
dolg = int(input('Долговых расписок:'))
friend_list = [0] * friends_count
print(friend_list)
for i in range(dolg):
    print(f'{i +1 }-я расписка')
    to_whom = int(input('Кому:'))
    from_whom = int(input('От кого:'))
    how_much = int(input('Сколько: '))
    friend_list[to_whom - 1] -= how_much
    friend_list[from_whom - 1] += how_much
print('Баланс друзей:')
for i in range(0, len(friend_list)):
    print(i + 1, ":", friend_list[i])

