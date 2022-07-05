text = open('zen.txt', 'r')
for i in reversed(list(text)):
    print(i, end='')
text.close()
