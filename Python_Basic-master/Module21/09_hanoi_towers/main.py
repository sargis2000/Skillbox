def tower_hanoii(count, a, b, c):
    if count == 1:
        print(f"Переложить диск 1 со стержня номер {a} на стержень номер {b}")
        return
    tower_hanoii(count - 1, a, c, b)
    print(f"Переложить диск {count} со стержня номер {a} на стержень номер {b} ")
    tower_hanoii(count - 1, c, b, a)


n = int(input('Введите количество дисков: '))
tower_hanoii(n, 1, 3, 2)
