with open('registrations.txt', 'r') as reg_file:
    with open('registrations_good.log', 'w') as good:
        with open('registrations_bad.log', 'w') as bad:
            for i in reg_file:
                try:
                    list_i = i.split()
                    if 10 > int(list_i[2]) or 99 < int(list_i[2]):
                        raise ValueError
                    if not list_i[0].isalpha():
                        raise NameError
                    if ('@' and '.') not in list_i[1]:
                        raise SyntaxError
                except ValueError:
                    bad.write(i.rstrip() + '\t' + 'Поле «Возраст» НЕ является числом от 10 до 99:\n')
                except IndexError:
                    bad.write(i.rstrip() + '\t' + 'НЕ присутствуют все три поля: \n')
                except NameError:
                    bad.write(i.rstrip() + '\t' + 'Поле имени содержит НЕ только буквы: \n')
                except SyntaxError:
                    bad.write(i.rstrip() + '\t' + 'Поле «Имейл» НЕ содержит @ и .(точку): \n')
                else:
                    good.write(i)



