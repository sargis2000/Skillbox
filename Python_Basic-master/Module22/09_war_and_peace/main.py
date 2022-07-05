import os
import sys
import collections
import zipfile


def dict_creator(txt):
    result = dict()
    for line in txt:
        for char in line:
            if char.isalpha():
                if char not in result:
                    result[char] = 0
                result[char] += 1
    return result


def dict_sorter(mydict):
    sorted_values = sorted(mydict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for val in sorted_values:
        for k in mydict.keys():
            if mydict[k] == val:
                sorted_dict[k] = val
    return sorted_dict


zfile = zipfile.ZipFile('voyna-i-mir.zip', 'r')
for i in zfile.namelist():
    zfile.extract(i)
    with open(i) as file:
        print(dict_sorter(dict_creator(file)))
        file.close()

    zfile.close()

