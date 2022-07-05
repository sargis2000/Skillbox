name = input('Eter your Name: ')
while True:
    choice = input('Enter 1 for: Посмотреть текущий текст чата.\n'
                   'Enter 2 for: Отправить сообщение \n')
    if choice == '1':
        try:
            with open('chat.txt', 'r') as read_file:
                for line in read_file:
                    print(line.strip())
        except FileNotFoundError:
            with open('chat.txt', 'w') as writefile:
                continue
    elif choice == '2':
        with open('chat.txt', 'a') as inputtxt:
            inputtxt.write(f'{name}: {input("Enter your message")}\n')
    else:
        print('Enter correct choice')
