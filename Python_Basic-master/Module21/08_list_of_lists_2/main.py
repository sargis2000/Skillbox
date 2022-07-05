nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
new_list = list()


def beauty_list(mylist, new_list):
    if isinstance(mylist, list):
        for i in mylist:
            if isinstance(i, list):
                beauty_list(i, new_list)
            else:
                new_list.append(i)
    return new_list


print(beauty_list(nice_list, new_list))
