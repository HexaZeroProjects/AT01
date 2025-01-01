import unittest
from main import remainder

class TestRemainder(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(15, 4), 3)
        self.assertEqual(remainder(22, 5), 2)

    def test_remainder_by_zero(self):
        self.assertRaises(ValueError, remainder, 10, 0)

if __name__ == '__main__':
    unittest.main()
