"""
    triangle-test.py

    TODO
    - [] 正三角形のときは1
    - [] 二等辺三角形のときは2
    - [] 不等辺三角形のときは3
    - [] 三角形でないときは例外
"""

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == "__main__":
    unittest.main()
