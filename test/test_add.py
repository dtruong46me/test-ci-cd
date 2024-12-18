import unittest

import os, sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from app.add import add

class TestAdd(unittest.TestCase):
    def test_main(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 1)
        self.assertEqual(add(0, 0), 0)