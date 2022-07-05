text = input('Введите строку: ').split(' ')
longest = max(text, key=len)
print("Самое длинное слово: {} \nДлина этого слова: {} ".format(longest, len(longest)))
