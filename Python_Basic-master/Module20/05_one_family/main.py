dict_of_FI = {
    ('Сидоров', 'Никита'): 15,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 24,
    ('Петров', 'Виктор'): 15,
    ('Петрова', 'Дарья'): 16,
    ('Петрова', 'Алина'): 33,
    ('Ляховский', 'Артём'): 41,

}


def fam(surname):
    tuple_of_ends = (('ов', 'ова'), ('ев', ' ева'), ('ий', 'ая'))
    for i, j in tuple_of_ends:
        if surname.endswith(i):
            return surname, surname[: -len(i)] + j
        elif surname.endswith(j):
            return surname, surname[: -len(j)] + i


lastname = input('Enter Surname:').capitalize()
for i, j in dict_of_FI.items():
    if i[0] in fam(lastname):
        print(i[0], i[1], j)
