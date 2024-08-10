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
print(single_root_words('Disablement',  'Mable', 'DisAble',  'Bagel', 'Able'))