import unittest
from Runner_1 import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results):
            result = cls.all_results[key]
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(f"{key}: {formatted_result}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertEqual(str(results[max(results.keys())]), "Ник", f"Expected last runner to be Ник, but got {results[max(results.keys())]}")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertEqual(str(results[max(results.keys())]), "Ник", f"Expected last runner to be Ник, but got {results[max(results.keys())]}")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertEqual(str(results[max(results.keys())]), "Ник", f"Expected last runner to be Ник, but got {results[max(results.keys())]}")

if __name__ == '__main__':
    unittest.main()