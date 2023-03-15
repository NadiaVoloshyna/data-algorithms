from unittest import TestCase
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(TestCase):
    def setUp(self):
        self.l1 = SinglyLinkedList()
        self.l1.append(3)
        self.l1.append(5)

    def test_getlist(self):
        self.assertEqual(self.l1.getlist(), [3,5])

    def test_size(self):
        self.assertEqual(self.l1.size, 2)

    def test_append(self):
        self.assertTrue(self.l1.append(7))
        self.assertEqual(self.l1.getlist(), [3,5,7])
        self.assertEqual(self.l1.size, 3)

    def test_insert(self):
        self.assertTrue(self.l1.insert(2,2))
        self.assertFalse(self.l1.insert(9,4))
        self.assertEqual(self.l1.getlist(), [3,2,5])

    def test_search(self):
        self.assertTrue(self.l1.search(3))
        self.assertFalse(self.l1.search(7))

    def test_delete(self):
        self.assertTrue(self.l1.delete(3))
        self.assertEqual(self.l1.getlist(), [5])

