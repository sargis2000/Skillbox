from collections import OrderedDict


class Student:
    def __init__(self, fl_name, group_number, academic_performance):
        self.fl_name = fl_name
        self.group = group_number
        self.per = sum(academic_performance) / 5


def obj_creator():
    name = input('enter ФИ')
    group = input('Номер группы ')
    performance = [int(i) for i in input('Успеваемость').split()]
    return Student(name, group, performance)


def dict_sorter(mydict):
    sorted_values = sorted(mydict.values(), reverse=True)
    sorted_dict = OrderedDict()
    for val in sorted_values:
        for k in mydict.keys():
            if mydict[k] == val:
                sorted_dict[k] = val
    return sorted_dict


obj_list = [obj_creator() for _ in range(3)]
obj_dict = dict_sorter({i.fl_name: i.per for i in obj_list})
for i in obj_dict:
    print(i)
