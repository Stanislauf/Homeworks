import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут, контролирующий заморозку тестов

    def test_example_1(self):
        # Пример теста
        self.assertTrue(True)

    def test_example_2(self):
        # Другой пример теста
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # тесты заморожены

    def test_example_3(self):
        # Пример теста
        self.assertTrue(True)

    def test_example_4(self):
        # Другой пример теста
        self.assertTrue(True)