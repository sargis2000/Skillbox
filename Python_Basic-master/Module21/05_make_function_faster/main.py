from time import time
dict_of_fac = {1: 1}


def calculating_math_func(data, mydict):
    if data not in mydict:
        result = max(mydict.values())
        for index in range(max(mydict.keys()) + 1, data + 1):
            result *= index
            mydict[index] = result
    else:
        result = mydict[data]
    result /= data ** 3
    result = result ** 10
    return result


time_work1 = time()
calculating_math_func(10, dict_of_fac)
time_work1 = time() - time_work1
time_work2 = time()
calculating_math_func(10, dict_of_fac)
time_work2 = time() - time_work2
print(time_work1 - time_work2)




