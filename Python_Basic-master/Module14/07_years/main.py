def main():
    first_number = input('Введите первый год: ')
    second_number = input('Введите первый год: ')
    if checker(first_number) and checker(second_number):
        finder(first_number, second_number)
    else:
        print("enter correct value")


def finder(num1, num2):
    num1, num2 = int(num1), int(num2)
    for i in range(num1, num2):
        for j in range(10):
            if str(i).count(str(j)) == 3:
                print(i)


def checker(num):
    if num.isdigit() and len(num) == 4:
        return True
    else:
        return False


main()
