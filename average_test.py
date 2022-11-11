# use unitest module for more comprehensive set of tests
import average
import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average.average([20, 30, 70]), 40.0)
        self.assertEqual(round(average.average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average.average([])
        with self.assertRaises(TypeError):
            average.average([20, 30, 70])


unittest.main()
