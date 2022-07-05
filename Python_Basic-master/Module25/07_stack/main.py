class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def __getitem__(self, item):
        return self.stack[item]

    def __setitem__(self, key, value):
        self.stack.insert(key, value)

    def __iter__(self):
        return iter(self.stack)


class Manager:
    def __init__(self):
        self.line = Stack()
        self.number = Stack()

    def new_task(self, obj1, obj2):
        self.line.push(obj1)
        self.number.push(obj2)

    def __str__(self):
        retun_str = ''
        for j in sorted(set(self.number)):
            retun_str += str(j) + ':'
            x = [i for i, val in enumerate(self.number) if val == j]
            for index in x:
                retun_str += f'{self.line[index]}\t'
            retun_str += '\n'

        return retun_str

    # def __iter__(self):
    #     return zip(self.line, self.number)


T = Manager()
T.new_task('Ankaptext', 7)
T.new_task('asdjkkasf', 8)
T.new_task('Nortext', 7)
T.new_task('Havesin,', 2)

print(T)

