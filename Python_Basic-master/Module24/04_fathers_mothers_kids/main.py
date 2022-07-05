class Parent:
    def __init__(self, name, age, *children_tup):
        self.name = name
        self.age = age
        self.children = list(children_tup)
        for i in self.children:
            if i.age > self.age - 16:
                print('He is not my childe:D!!!')
                self.children.remove(i)

    def info(self):
        print(f'My name is {self.name}.\nI"m {self.age} years old.\nMy children are {self.children}')

    def calm(self):
        for i in self.children:
            i.calm = True

    def feed(self):
        for i in self.children:
            i.hunger = True


class Child:
    def __init__(self, name, age,  calm=False, hunger=False):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

