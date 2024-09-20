import io
class WordsFinder:

    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:    # открываем файл
                text = file.read()                             #
                for char in chars_to_remove:                      # убираем ненужные символы в тексте
                    text = text.replace(char, '')
            with open(name, 'w', encoding='utf-8') as file:
                file.write(text)
                words = []
                for line in text.splitlines():        #
                    for word in line.split():         # разделяем слова
                        words.append(word.lower())    # добавляем слова в список
                all_words[name] = words               # создаем словарь
        return all_words
    def find(self, word):
        word = word.lower()
        position = {}
        for file_name, words in self.get_all_words().items(): # перебираем ключ значение в готовом словаре
            if word in words:                                 # из предыдущего метода
                position[file_name] = words.index(word) + 1   # создаем словарь {название файла : позиция искомого слова}
        return position

    def count(self, word):
        word = word.lower()
        count = {}
        k = 0
        for file_name, words in self.get_all_words().items():
             # count[file_name] = words.count(word) # можно короче
            for i in words:
                if word == i:
                    k += 1
                count[file_name] = k
            k = 0
        return count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TExT'))
print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))