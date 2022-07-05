def can_be_poly(word):
    from collections import Counter
    count = 0

    for i in Counter(word).values():
        if count <= 1:
            if i % 2 != 0:
                count += 1
        else:
            return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))