import unittest
import tests_12_3

my_test_suite = unittest.TestSuite()
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

unittest.TextTestRunner(verbosity=2).run(my_test_suite)