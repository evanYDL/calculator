import unittest
from calculator import eval_expr

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(eval_expr('1 + 2'), 3)

    def test_precedence(self):
        self.assertEqual(eval_expr('2 + 3 * 4'), 14)

    def test_parentheses(self):
        self.assertEqual(eval_expr('(2 + 3) * 4'), 20)

    def test_unary(self):
        self.assertEqual(eval_expr('-5 + 2'), -3)

if __name__ == '__main__':
    unittest.main()
