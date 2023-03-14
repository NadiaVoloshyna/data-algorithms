from unittest import TestCase
from point import Point


class TestPoint(TestCase):

    def setUp(self):
        self.p1 = Point(1,1)

    def test_distance1(self):
        self.p2 = Point(2, 2)
        self.assertEqual(self.p1.distance(self.p2), 1.4142135623730951)

    def test_distance2(self):
        self.p2 = Point(3, 3)
        self.assertEqual(self.p1.distance(self.p2), 2.8284271247461903)
        self.p3 = Point(4, 4)
        self.assertEqual(self.p1.distance(self.p3), 4.242640687119285)

# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()