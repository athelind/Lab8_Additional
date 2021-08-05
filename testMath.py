import unittest
from mathA import Operation

class testMath(unittest.TestCase):

    def test_add(self):
        result = Operation.add(1, 2)
        self.assertEqual(result, 3)

    def test_minus(self):
        pass

    def test_divide(self):
        pass

    def test_product(self):
        pass