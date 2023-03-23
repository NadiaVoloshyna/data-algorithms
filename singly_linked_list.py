"""
https://learning.oreilly.com/library/view/hands-on-data-structures/9781801073448/Text/Chapter_4.xhtml#_idParaDest-78
https://study.online.abertay.ac.uk/courses/194/discussion_topics/1175 (Steve Helmore)
15/03/2023
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def __str__(self):
        return "head:" + str(self.head.data) + " tail:" + str(self.tail.data) + " size:" + str(self.size)

    def get_list(self):
        l = []
        for node in self.iter():
            l.append(node)
        return l

    def size(self):
        return self.size

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.size += 1
            return True
        else:
            self.head = node
            self.tail = node
            self.size += 1
            return True

    def insert(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        if index < 1 or index > self.size:
            print("Index is out of range")
            return False
        while current:
            if index == 1:
                node.next = current
                self.head = node
                self.size += 1
                return True
            elif count == index:
                node.next = current
                prev.next = node
                self.size += 1
                return True
            prev = current
            current = current.next
            count += 1

    def search(self, data):
        for node in self.iter():
            if node == data:
                print("Found")
                return True
        print("Not found")
        return False

    def delete(self, data):
        if self.head == None:
            print("List is empty")
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            current = current.next
            prev = current

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

def linked_list_demo():
    l = SinglyLinkedList()
    print("initial: " + str(l.get_list()))
    l.append(3)
    l.append(5)
    l.append(7)
    print("after append: " + str(l.get_list()))
    l.insert(2,2)
    print("after insertion: " + str(l.get_list()))
    l.insert(1,5)
    l.insert(9,1)
    print("after insertion at the beginning: " + str(l.get_list()))
    l.search(9)
    l.search(11)
    l.delete(9)
    print("after delete: " + str(l.get_list()))

linked_list_demo()
