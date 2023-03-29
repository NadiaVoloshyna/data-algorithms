from unittest import TestCase
from binary_search import is_sorted

class Test(TestCase):
    def setUp(self):
        self.l1 = [1,2,3,4,5]
        self.l2 = [6,8,4,5,3]

    def test_is_sorted1(self):
        self.assertTrue(is_sorted(self.l1))

    def test_is_sorted2(self):
        self.assertFalse(is_sorted(self.l2))
