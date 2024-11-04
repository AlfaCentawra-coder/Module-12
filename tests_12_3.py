import unittest
from Runner import Runner
from Runner_1 import Runner as Runner_1, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner_1("Усэйн", 10)
        self.andrey = Runner_1("Андрей", 9)
        self.nick = Runner_1("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results):
            result = cls.all_results[key]
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(f"{key}: {formatted_result}")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertEqual(str(results[max(results.keys())]), "Ник", f"Expected last runner to be Ник, but got {results[max(results.keys())]}")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertEqual(str(results[max(results.keys())]), "Ник", f"Expected last runner to be Ник, but got {results[max(results.keys())]}")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertEqual(str(results[max(results.keys())]), "Ник", f"Expected last runner to be Ник, but got {results[max(results.keys())]}")

if __name__ == '__main__':
    unittest.main()