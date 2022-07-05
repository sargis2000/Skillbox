def reversing(n, k, index):
    n = n.split('.')[index]
    k = k.split('.')[index]
    return int(n[:: -1]), int(k[:: -1])


def main():
    N = input('Enter the First number: ')
    K = input("Enter second number: ")

    try:
        N = str(float(N))
        K = str(float(K))
        whole = reversing(N, K, 0)
        after_point = reversing(N, K, 1)
        summ = f'{sum(whole)}.{sum(after_point)}'
        print(f'Первое число наоборот:{whole[0]}.{after_point[0]}')
        print(f'Второе число наоборот:{whole[1]}.{after_point[1]}')
        print('Сумма:', summ)
    except ValueError:
        print("enter correct values")
        main()


main()
