import unittest

import os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from app.main import add, substract

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

        self.assertEqual(substract(2, 3), -1)
        self.assertEqual(substract(-1, 1), -2)
        self.assertEqual(substract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()