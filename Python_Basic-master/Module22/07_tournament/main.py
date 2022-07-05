def dict_sorter(mydict):
    sorted_values = sorted(mydict.values(), reverse=True)
    sorted_dict = {}
    for val in sorted_values:
        for k in mydict.keys():
            if mydict[k] == val:
                sorted_dict[k] = val
                break
    return sorted_dict


def dict_creator(text):
    dict_members = dict()
    for i in text:
        try:
            min_val = int(i)
        except ValueError:
            i = i.split()
            if int(i[2]) > min_val:
                dict_members[(i[0], i[1])] = int(i[2])
    return dict_sorter(dict_members)


with open('first_tour.txt', 'r') as txt:
    context = dict_creator(txt)
    txt.close()
with open('second_tour.txt:', 'w') as file:
    text = f'{len(context)}\n'
    for i, j in enumerate(context.keys()):
        text += f'{i + 1}) {j[1][0]}. {j[0]} {context[j]}\n'
    file.write(text)
    file.close()
