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

    def getType(self):
        if (self.a == self.b and self.b == self.c):
            return 1
        if (self.a == self.b or self.b == self.c or self.a == self.c):
            return 2


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        triangle = Triangle(10, 10, 10)
        self.assertEqual(1, triangle.getType())

    def test_isosceles(self):
        triangle = Triangle(10, 10, 5)
        self.assertEqual(2, triangle.getType())


if __name__ == "__main__":
    unittest.main()
