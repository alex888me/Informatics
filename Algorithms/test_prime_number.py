import unittest
from prime_number import is_prime

class TestPrimeMethods(unittest.TestCase):
    def test_is_prime(self):
        # Known prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))

        # Known non-prime numbers
        self.assertFalse(is_prime(1))  # By definition, 1 is not a prime
        self.assertFalse(is_prime(4))  # Even number greater than 2
        self.assertFalse(is_prime(6))  # Divisible by 2 and 3
        self.assertFalse(is_prime(8))  # Even number greater than 2
        self.assertFalse(is_prime(9))  # Square of a prime (3)
        self.assertFalse(is_prime(15)) # Divisible by 3 and 5
        self.assertFalse(is_prime(16)) # Even number greater than 2

        # Very large prime
        self.assertTrue(is_prime(104729))  # Known to be the 10000th prime

        # Very large non-prime
        self.assertFalse(is_prime(104730)) # Just above the 10000th prime

if __name__ == '__main__':
    unittest.main()
