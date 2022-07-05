from random import randint


class Men:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.house = House()

    def eat(self):
        print(f'{self.name} eating')
        self.satiety += 1
        self.house.food -= 1

    def work(self):
        print(f'{self.name} working')
        self.satiety -= 1
        self.house.money += 1

    def play(self):
        print(f'{self.name} playing')
        self.satiety -= 1

    def shopping(self):
        print(f'{self.name} shopping')
        self.house.food += 1
        self.house.money -= 1

    def live(self):
        if self.satiety < 0:
            print('!!!!!!!!!!RIP!!!!!')
            return False
        else:
            choice = randint(1, 6)
            if self.satiety < 20:
                self.eat()
            elif self.house.food < 10:
                self.shopping()
            elif self.house.money < 50:
                self.work()
            elif choice == 1:
                self.work()
            elif choice == 2:
                self.eat()
            else:
                self.play()
            return True


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


men1 = Men('Artem')
men2 = Men('Sargis')
for i in range(365):
    print(f'Day {i + 1}')
    if not men1.live():
        break
    if not men2.live():
        break
else:
    print('We still Alive')
