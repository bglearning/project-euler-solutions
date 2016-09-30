import unittest
from prime import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `prime.py`."""

    def test_is_one_not_prime(self):
        """Is one successfully determined to be not prime?"""
        self.assertFalse(is_prime(1))

    def test_is_minus_one_not_prime(self):
        """Is minus one successfully determined to be not prime?"""
        self.assertFalse(is_prime(-1))

    def test_is_two_prime(self):
        """Is two successfully determined to be prime?"""
        self.assertTrue(is_prime(2))

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_seventy_three_prime(self):
        """Is seventy-three successfully determined to be prime?"""
        self.assertTrue(is_prime(73))

if __name__=='__main__':
    unittest.main()
