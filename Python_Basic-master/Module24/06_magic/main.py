class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()


class Shtorm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Dirt:
    name = 'Грязь'


class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


a = Water()
b = Air()
s = a + b

print(f"Смешиваем '{a.name}' c '{b.name}' и получаем '{s.name}'")

