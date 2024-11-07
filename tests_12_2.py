import unittest
from runner import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", speed=10)
        self.runner2 = Runner("Andrey", speed=9)
        self.runner3 = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({place: str(participant) for place, participant in result.items()})

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results
        self.assertTrue(results[max(results.keys())] == self.runner3)

# Запускаем тесты
if __name__ == "__main__":
    unittest.main()