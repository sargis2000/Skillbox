from random import randint, choice


class Home:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.food_for_cat = 30
        self.dirty = 0


class Person(Home):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.satiety = 30
        self.happiness = 10

    def kity_kity_cat(self):
        self.happiness += 5
        return self.happiness

    def eat(self):
        ate = randint(1, 30)
        self.food -= ate
        self.satiety += ate * 2
        return ate


class Men(Person):
    def play(self):
        self.satiety -= 10
        self.happiness += 20

    def work(self):
        self.satiety -= 10
        self.money += 150
        return 150


class Women(Person):
    def buy_food(self, mode='Person'):
        self.satiety -= 10
        self.money -= 10
        if mode == 'Person':
            self.food += 10
        elif mode == 'Cat':
            self.food_for_cat += 10

    def buy_fur_coat(self):
        self.satiety -= 10
        self.money -= 350
        self.happiness += 60
        return 1

    def clean_home(self):
        self.satiety -= 10
        self.dirty -= 100


class Cat(Home):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.satiety = 30

    def sleep(self):
        self.satiety -= 10

    def tear(self):
        self.satiety -= 10
        self.dirty += 5

    def eat(self):
        ate = randint(1, 10)
        self.food -= ate
        self.satiety += ate * 2
        return ate


men = Men('Davide')
woman = Women('Anna')
cat = Cat('Kiska')

shoub_count = 0
food_count = 0
worked_money = 0


def men_did(men):
    global food_count
    global worked_money
    if men.satiety <= 0:
        food_count += men.eat()
    elif men.happiness <= 10:
        if men.happiness >= 5:
            men.kity_kity_cat()
        else:
            men.play()
    else:
        worked_money += men.work()


def women_did(women):
    global food_count
    global shoub_count
    if women.happiness <= 10:
        if men.happiness >= 5:
            shoub_count += women.kity_kity_cat()
        else:
            women.buy_fur_coat()
    elif women.satiety <= 0:
        food_count += women.eat()
    elif women.dirty >= 100:
        women.clean_home()
    else:
        if choice([1, 2]) == 2:
            women.buy_food(mode='Cat')
        else:
            women.buy_food()


def cat_did(cat):
    global food_count
    if cat.satiety <= 0:
        food_count += cat.eat()
    elif choice([1, 2]) == 1:
        cat.sleep()
    else:
        cat.tear()


for i in range(365):
    Home().dirty += 5
    men_did(men)
    women_did(woman)
    cat_did(cat)

print(food_count)
print(worked_money)
print(shoub_count)
