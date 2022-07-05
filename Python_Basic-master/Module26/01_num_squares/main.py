from collections.abc import Iterable
N = int(input('Enter thy number'))


class Square:
    def __init__(self, n: int) -> None:
        self.n = 0
        self.next = 0
        self.stop = n

    def __iter__(self) -> Iterable:
        self.n = 0
        self.next = 0
        return self

    def __next__(self) -> Iterable:
        if self.n == self.stop:
            raise StopIteration
        self.n, self.next = self.next, self.next + 1
        return self.n ** 2


def square(stop: int) -> Iterable:
    num = 0
    for _ in range(stop + 1):
        yield num ** 2
        num += 1


a = (i ** 2 for i in range(0, N + 1))
for i in a:
    print(i)
print('--------------------------------------------------')
for i in Square(N):
    print(i)
print('--------------------------------------------------')
for i in square(N):
    print(i)


