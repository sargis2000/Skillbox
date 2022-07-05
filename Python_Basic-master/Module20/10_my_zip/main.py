mystr = 'abcd'
mytuple = (10, 20, 30, 40)

print((i, j) for i, j in zip(mystr, mytuple))
for i in zip(mystr, mytuple):
    print(i)


def myzip(obj1, obj2):
    if len(obj1) > len(obj2):
        obj2 = obj2[:len(obj1)]
    elif len(obj1) < len(obj2):
        obj1 = obj1[:len(obj2)]
    return ((obj1[i], obj2[i])for i in range(len(obj1)))

print(myzip(mystr, mytuple))
print((i, j) for i, j in myzip(mystr, mytuple))
for i in myzip(mystr, mytuple):
    print(i)