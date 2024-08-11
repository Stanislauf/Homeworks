def single_root_words(root_word, *other_words):
    same_words = []
    for j in range(len(other_words)):
        if other_words[j].lower() in root_word.lower():
            root_word = other_words[j]
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower():
            if root_word.lower() == other_words[i].lower():
                continue
            same_words.append(other_words[i].lower())
    return same_words


print(single_root_words('гРиб', 'ГрибниК', 'гриБок', 'мУхоМор', 'грИбной', 'доЖдь', 'гРиб'))
print(single_root_words('Disablement', 'Mable', 'DisAble', 'Bagel', 'Able'))
print(single_root_words('крас', 'прекрасный', 'красный', 'кран', 'красивый'))

# 2 вариант для самостоятельного ввода проверочных слов и корня
print('______________________________________________________')

def single_root_words_2(root_word, other_words):
    same_words = []
    for j in range(len(other_words)):
        if other_words[j].lower() in root_word.lower():
            root_word = other_words[j]
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower():
            if root_word.lower() == other_words[i].lower():
                continue
            same_words.append(other_words[i].lower())
    return same_words

root_word = input('Введите корерь искомого слова: ')
other_words = input('Введите остальные слова через пробел: ')

other_words_2 = []
word = ''
for i in range(0, len(other_words)):
    if other_words[i] != ' ':
        word = word + other_words[i]
        if i == len(other_words) - 1:
            other_words_2.append(word)
            break
    else:
        other_words_2.append(word)
        word = ''
print(single_root_words_2(root_word, other_words_2))
