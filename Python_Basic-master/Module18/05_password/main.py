while True:
    password = input('Придумайте пароль: ')
    if sum(c.isdigit() for c in password) >= 3 and sum(a.isupper() for a in password) >= 1:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')