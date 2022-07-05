from string import punctuation
text = input('Сообщение: ').split(' ',)
newtxt = ''
counter = 0
for i in range(len(text)):
    if text[i].isalpha():
        newtxt += text[i][:: -1] + ' '
    else:
        for sym in punctuation:
            if sym in text[i]:
                counter += 1
        if len(text[i]) != counter:
            new_str = ''
            for sym in punctuation:
                if sym in text[i]:
                    sym_idex = text[i].find(sym)
                    new_str = text[i][sym_idex - 1::-1] + sym + text[i][:sym_idex:-1]
                    newtxt += new_str + ' '
        else:
            newtxt += text[i] + ' '
            counter = 0

print('Новое сообщение: ', newtxt)
