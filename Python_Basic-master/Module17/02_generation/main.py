lenght = int(input('Введите длину списка: '))
result = [i % 5 if i % 2 == 1 else 1 for i in range(lenght)]
print('Результат: ', result)
