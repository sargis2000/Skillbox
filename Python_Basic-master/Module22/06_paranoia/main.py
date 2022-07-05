from string import ascii_uppercase, ascii_lowercase
lower_alphabet = ascii_lowercase
upper_alphabet = ascii_uppercase


def caesar():
    with open('text.txt', 'r') as file:
        print('Содержимое файла text.txt:')
        iter_count = 0
        for i in file:
            iter_count += 1
            print(i, end='')
        file.seek(0)
        new_txt = ''
        for line, j in zip(file, range(1, iter_count + 1)):
            for char in line:
                if char in lower_alphabet:
                    lower = lower_alphabet[j:] + lower_alphabet[:j]
                    new_txt += lower[lower_alphabet.index(char)]
                elif char in upper_alphabet:
                    upper = upper_alphabet[j:] + upper_alphabet[:j]
                    new_txt += upper[upper_alphabet.index(char)]
                else:
                    new_txt += char
        with open(' cipher_text.txt:', 'w+') as file_write:
            file_write.write(new_txt)
            file_write.seek(0)
            print('Содержимое файла cipher_text.txt::')
            for i in file_write:
                print(i, end='')
            file_write.close()
        file.close()


caesar()

