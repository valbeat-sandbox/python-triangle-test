"""
    triangle-test.py

    TODO
    - [] 正三角形のときは1
    - [] 二等辺三角形のときは2
    - [] 不等辺三角形のときは3
    - [] 三角形でないときは例外
"""

import unittest


class Triangle():

    def __init__(self, a, b, c):
        # 取り敢えず辺の長さ
        self.a = a
        self.b = b
        self.c = c


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        triangle = Triangle(10, 10, 10)
        self.assertTrue(triangle.a == triangle.b and triangle.b == triangle.c)


if __name__ == "__main__":
    unittest.main()
