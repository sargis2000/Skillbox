class Potato:
    def __init__(self, index):
        self.index = index
        self.state = 0

    def info(self):
        print(f'Potato {self.index} in state {self.state}')
        if self.state < 3:
            return True
        else:
            return False

    def grew_up(self):
        self.info()
        if self.state < 3:
            self.state += 1
            return True
        else:
            return False


class Gardener:
    def __init__(self, name, garden, *potato_indexes, mode='All'):
        self.name = name
        self.garden = garden
        self.mode = mode
        self.potato_indexes = list(potato_indexes)

    def take_care_of(self):
        if self.mode == 'All':
            self.garden.grow_all()
        else:

            for i in self.garden.list_potatoes:
                if i.index in self.potato_indexes:
                    i.grew_up()

    def harvest(self):
        print('we havest the garden')
        self.garden.list_potatoes = list()


class Garden:
    def __init__(self, pot_count):
        self.list_potatoes = [Potato(index) for index in range(1, pot_count + 1)]

    def grow_all(self):
        for i in self.list_potatoes:
            while True:
                boolean = i.grew_up()
                if not boolean:
                    break

    def get_all_info(self):
        if True in [i.info() for i in self.list_potatoes]:
            print('Not all Grew up')
        else:
            print('All grew up')


garden = Garden(5)
garden.get_all_info()
print('-------------------------')
garden.grow_all()
garden.get_all_info()
Gardener('Artem', garden, 1, 2, mode='Anymod').take_care_of()
garden.get_all_info()
Gardener('Artem', garden, mode='All').take_care_of()
garden.get_all_info()
Gardener('Artem', garden, mode='All').harvest()
print(garden.list_potatoes)


