import unittest
from runner import Runner, Tournament  # Импортируем необходимые классы
from tests_12_3 import RunnerTest, TournamentTest

# Декоратор для пропуска тестов
def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print("Тесты в этом кейсе заморожены")
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_method(self, *args, **kwargs)
    return wrapper

# Обновление методов тестирования в классе RunnerTest
for name, method in RunnerTest.__dict__.items():
    if callable(method) and not name.startswith('__'):
        setattr(RunnerTest, name, skip_if_frozen(method))

# Обновление методов тестирования в классе TournamentTest
for name, method in TournamentTest.__dict__.items():
    if callable(method) and not name.startswith('__'):
        setattr(TournamentTest, name, skip_if_frozen(method))

# Создание объекта TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Запуск тестов с помощью TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)