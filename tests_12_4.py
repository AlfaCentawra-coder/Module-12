import logging
import unittest
from rt_with_exception import Runner


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_test.log",
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("TestRunner", speed=-10)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info("'TestWalk' выполнен успешно")
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info("'TestRun' выполнен успешно")
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
