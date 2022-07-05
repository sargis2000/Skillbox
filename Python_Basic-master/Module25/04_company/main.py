class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.sales_volume = sales_volume

    def salary(self):
        return 5000 + 5 * self.sales_volume / 100


class Worker(Employee):
    def __init__(self, name, surname, age, work_time):
        super().__init__(name, surname, age)
        self.work_time = work_time

    def salary(self):
        return 100 * self.work_time


list_persons = [
    Manager('Saqo', 'Khachatryan', 21),
    Manager('ESem', 'Inchvorban', 36),
    Manager('Ankap', 'Anun', 37),
    Worker('tsdfazsdfa', 'anfdsun', 25, 100),
    Worker('tafsdza', 'anfsdun', 70, 89),
    Worker('LOl', 'lolov', 11, 67),
    Agent('MMlol', 'Totin', 35, 10000),
    Agent('Mfunin', 'Funin', 15, 108000),
    Agent('AAAol', 'TXXXin', 15, 108000)
]

list_salary = [i.salary() for i in list_persons]
print(list_salary)
print('Max. Salary', max(list_salary))


