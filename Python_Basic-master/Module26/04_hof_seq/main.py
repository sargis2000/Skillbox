from collections.abc import Iterable


class Q:
    def __init__(self, s: list) -> None:
        self.s = list(reversed(s))

    def __next__(self) -> Iterable:
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> Iterable:
        return self


Q = Q([1, 1])

for i in Q:
    if i < 1000:
        print(i)
    else:
        break
