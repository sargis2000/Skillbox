def caesar(txt, shift,):
    new_russian_alphabet = russian_alphabet[shift:] + russian_alphabet[:shift]
    for i in txt:
        if i in russian_alphabet:
            print(new_russian_alphabet[russian_alphabet.index(i)], end='')
        else:
            print(i, end='')


russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
text = input('Введите сообщение: ')
key = int(input('Введите сдвиг: '))



caesar(text, key)
