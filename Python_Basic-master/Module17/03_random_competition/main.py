import random
list1 = [round(random.uniform(33.33, 66.66), 2) for _ in range(10)]
list2 = [round(random.uniform(33.33, 66.66), 2) for _ in range(10)]
list3 = [max(list1[i], list2[i]) for i in range(10)]
print('Первая команда: ', list1, '\nВторая команда:  ', list2, '\nПобедители тура:', list3)