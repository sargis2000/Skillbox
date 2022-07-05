file_read = open('numbers.txt', 'r')
file_write = open('answer.txt', 'w')

summ = 0
for i in file_read:
    if i != '\n':
        summ += int(i.strip())
file_write.write(str(summ))
file_write.close()
file_read.close()