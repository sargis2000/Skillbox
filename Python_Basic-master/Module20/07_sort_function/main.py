def tpl_sort(tpl):
    for i in tpl:
        try:
            int(i)
        except ValueError:
            return tpl
    return tuple(sorted(tpl))


test_tuple = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(test_tuple))