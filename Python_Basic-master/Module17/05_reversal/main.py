mystring = input('Введите строку:').lower()
# first_h = mystring.index('h')
# second_h = mystring[:: -1].index('h')
# print(mystring[second_h: first_h: -1])
res = [i for i, item in enumerate(mystring) if item == 'h']
print(mystring[res[-1] - 1: res[0]: -1])
