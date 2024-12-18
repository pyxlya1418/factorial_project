import unittest
from factorial_module import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        """Тест факторіалу 0: очікується результат 1"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        """Тест факторіалу для додатних чисел"""
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        """Тест для від'ємних чисел: очікується ValueError"""
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_large_number(self):
        """Тест для великого числа"""
        self.assertEqual(factorial(10), 3628800)

if __name__ == "__main__":
    unittest.main()
