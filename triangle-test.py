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
        if (a <= 0 or b <= 0 or c <= 0):
            raise Exception('辺の長さが不正')
        if (a + b < c or a + c < b or b + c < a):
            raise Exception('2辺の和が不正')

        self.a = a
        self.b = b
        self.c = c

    def getType(self):
        if (self.a == self.b and self.b == self.c):
            return 1
        if (self.a == self.b or self.b == self.c or self.a == self.c):
            return 2
        return 3


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        triangle = Triangle(3, 3, 3)
        self.assertEqual(1, triangle.getType())

    def test_isosceles(self):
        triangle = Triangle(3, 3, 5)
        self.assertEqual(2, triangle.getType())

    def test_scalene(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(3, triangle.getType())

    def test_nodeLength(self):
        with self.assertRaises(Exception):
            Triangle(0, 3, 5)

    def test_nodeAdd(self):
        with self.assertRaises(Exception):
            Triangle(1, 3, 5)


if __name__ == "__main__":
    unittest.main()
