while True:
    IP = input('Введите IP: ').split('.')
    if len(IP) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        for i in IP:
            if not i.isdigit():
                print(f'{i} — это не целое число.')
                break
            elif int(i) > 255:
                print(f'{i} превышает 255.')
                break
        else:
            print('IP-адрес корректен.')
            break