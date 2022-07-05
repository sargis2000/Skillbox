def myzip(obj1, obj2):
    return ((obj1[iter_i], obj2[iter_i]) for iter_i in range(min(len(obj1), len(obj2))))


print(myzip([1, 2, 3, 88, 8, 8, 8, 8], 'abc'))
for i, j in myzip([1, 2, 3, 88, 8, 8, 8, 8], 'abc'):
    print(i, j)