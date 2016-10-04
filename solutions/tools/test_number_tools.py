import unittest
from number_tools import is_palindrome
from number_tools import divisors


class NumberToolsTestCase(unittest.TestCase):
    """Tests for `number_tools.py`."""

    """is_palindrome() tests"""
    def test_is_1224_palindrome(self):
        self.assertFalse(is_palindrome(1224))

    def test_is_1441_palindrome(self):
        self.assertTrue(is_palindrome(1441))

    def test_is_14567_palindrome(self):
        self.assertFalse(is_palindrome(14567))

    def test_is_456654_palindrome(self):
        self.assertTrue(is_palindrome(456654))

    def test_is_five_palindrome(self):
        self.assertTrue(is_palindrome(5))

    """divisors() tests"""
    def test_divisors_six(self):
        self.assertEqual(sorted(list(divisors(6))), [1, 2, 3])

    def test_divisors_twelve(self):
        self.assertEqual(sorted(list(divisors(12))), [1, 2, 3, 4, 6])

    def test_divisors_twelve_not_proper(self):
        self.assertEqual(sorted(list(divisors(10, False))), [1, 2, 5, 10])

if __name__ == '__main__':
    unittest.main()
