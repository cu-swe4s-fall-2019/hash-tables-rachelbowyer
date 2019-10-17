import unittest
import hash_functions as h
import random


class TestHashFunctions(unittest.TestCase):
    """testing hash functions types"""

    def test_h_ascii_works(self):
        """test h_ascii function returns expected result"""
        N = random.randint(1, 1000)  # chose rand file size
        r = h.h_ascii('testkey', N)  # test on known key
        self.assertEqual(r, sum(map(ord, 'testkey')) % N)

    def test_h_rolling_works(self):
        """test h_rolling function returns expected result"""
        N = random.randint(1, 1000)  # chose rand file size
        r = h.h_rolling('testkey', N)  # test on known key
        p = 53
        m = 2**64
        r2 = 0
        for i in range(len('testkey')):
            r2 += ord('testkey'[i]) * p**i
        r2 = r2 % m
        self.assertEqual(r, r2 % N)

    def test_h_python_works(self):
        """test h_python function returns expected result"""
        N = random.randint(1, 1000)  # chose rand file size
        r = h.h_python('testkey', N)  # test on known key
        self.assertEqual(r, hash('testkey') % N)


if __name__ == '__main__':
    unittest.main()
