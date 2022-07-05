from random import randint
from time import time
start_time = time()
original_list = [randint(0, 10) for _ in range(10)]
new_list = [
    (original_list[i], original_list[j])
    for i, j in zip(range(0, 10, 2), range(1, 10, 2))
]
print('Оригинальный список:', original_list)
print('Новый список:', new_list)
print(start_time - time())
print('------------------------------------')

start_time = time()
new_list = [
    (original_list[i], original_list[i + 1])
    for i in range(0, 10, 2)
]
print('Оригинальный список:', original_list)
print('Новый список:', new_list)
print(start_time - time())
