from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Сравниваем символы строк
result = list(map(lambda x, y: x == y, first, second))
print(result)  # Ожидаемый результат: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(f"{item}\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Класс MysticBall с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

# Использование класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайный выбор из предложенных слов
print(first_ball())
print(first_ball())