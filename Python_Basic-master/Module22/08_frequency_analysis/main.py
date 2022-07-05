from string import ascii_uppercase


def myfunc(file):
    chars_dict = dict()
    for line in file:
        line = line.upper()
        for i in ascii_uppercase:
            item = chars_dict.get(i, False)
            if not item:
                chars_dict[i] = line.count(i)
            else:
                chars_dict[i] = item + line.count(i)
    return {key: val for key, val in chars_dict.items() if val != 0}


def dict_sorter(mydict):
    sorted_values = sorted(mydict.values(), reverse=True)
    sorted_dict = {}
    for val in sorted_values:
        for k in mydict.keys():
            if mydict[k] == val:
                sorted_dict[k] = val
    return sorted_dict


with open('text.txt', 'r') as file:
    mydict = myfunc(file)
    mydict = dict_sorter(mydict)
    print(mydict)
    with open('analysis.txt:', 'a') as writing_file:
        for i in mydict.keys():
            mystring = f'{i} {round(mydict[i] / sum(mydict.values()), 3)}\n'
            writing_file.write(mystring)
        writing_file.close()
    file.close()
