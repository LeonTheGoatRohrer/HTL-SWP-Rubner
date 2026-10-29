import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        c = Calc()
        self.assertEqual(c.add(2, 3), 5)
