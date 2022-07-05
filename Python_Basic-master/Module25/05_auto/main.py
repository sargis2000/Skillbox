from math import sin, cos


class Auto:
    def __init__(self, x, y, alpha):
        self.x = x
        self.y = y
        self.alpha = alpha

    def move(self, distance, betta=None):
        if betta is not None:
            self.alpha += betta
        self.x += distance * cos(self.alpha)
        self.y += distance * sin(self.alpha)


class Bus(Auto):
    def __init__(self, x, y, alpha, money=0, passengers=0):
        super().__init__(x, y, alpha)
        self.money = money
        self.passengers = passengers

    def to_come_in(self):
        self.passengers += 1

    def to_come_out(self):
        if self.passengers > 0:
            self.passengers -= 1

    def move(self, distance, betta=None):
        Auto.move(distance, betta)
        self.money += distance * self.passengers





































