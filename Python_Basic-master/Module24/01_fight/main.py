from random import choice


class Warrior:
    def __init__(self, warrior_name):
        self.health = 100
        self.hit_point = 20
        self.warrior_name = warrior_name

    def attaced(self):
        if self.health > 0:
            self.health -= self.hit_point
            return self.health


obj1 = Warrior(warrior_name='warrior 1')
obj2 = Warrior(warrior_name='warrior 2')
arr_objs = (obj1, obj2)

iter_count = 1
while True:
    defender = choice(arr_objs)
    if defender.health > 0 and obj1.health > 0 and obj2.health > 0:
        print(f'Starts {iter_count} round')
        iter_count += 1
        if defender == obj1:
            print('Beat', obj2.warrior_name)
        else:
            print('Beat', obj1.warrior_name)
        defender.attaced()
        print(f'{defender.warrior_name} have {defender.health}')
    else:
        if defender == obj1:
            print('Win', obj2.warrior_name)
        else:
            print('Win', obj1.warrior_name)
        break




