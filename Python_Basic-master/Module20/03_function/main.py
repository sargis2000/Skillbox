def slicer(obj, index):
    count = obj.count(index)
    if index in obj and count >= 2:
        return obj[obj.index(index): obj.index(index, 2) + 1]
    elif count == 1:
        return obj[obj.index(index):]
    else:
        return ()


print(
    slicer(
        (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10),
        int(input('Enter Thr number: '))
    )
)
