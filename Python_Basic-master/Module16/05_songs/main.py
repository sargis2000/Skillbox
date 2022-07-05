violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

time = 0
count_songs = int(input('Сколько песен выбрать? '))
for i in range(count_songs):
    while True:
        name_song = input(f'Название {i + 1}-й песни:')
        for j in violator_songs:
            if j[0] == name_song:
                time += j[1]
                break
        else:
            print('Enter valid name')
            continue
        break

print('Общее время звучания песен: ', round(time, 2))
