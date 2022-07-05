students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
length_of_fam = 0
mylist = []
list_of_interests = []
for i, j in students.items():
    mylist.append((i, j["age"]))
    list_of_interests.extend(j['interests'])
    length_of_fam += len(j['surname'])
print(mylist)
print(list_of_interests)
print(length_of_fam)
