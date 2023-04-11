import random

class Node():
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree():
    def __init__(self):
        self.root_node = None
        self.nodes_counter = 0
        self.steps_counter = 0

    def insert(self, data):
        node = Node(data)
        if not self.root_node:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if not current:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if not current:
                        parent.right_child = node
                        return self.root_node

    def get_node_with_parent(self, data):
        current = self.root_node
        parent = None
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
                if not current:
                    return (None, None)
            else:
                parent = current
                current = current.right_child
                if not current:
                    return (None, None)

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        # get children count
        if node.left_child and node.right_child:
            children = 2
        elif node.left_child or node.right_child:
            children = 1
        else:
            children = 0

        if children == 0:
            if parent:
                if parent.left_child == node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None
        elif children == 1:
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child == node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        current = self.root_node

        while True:
            if current is None:
                return None
            elif current.data == data:
                return (data, self.steps_counter)
            elif current.data > data:
                current = current.left_child
                self.steps_counter += 1
            else:
                current = current.right_child
                self.steps_counter += 1

    def count(self, root_node):
        """returns the number of Nodes"""
        current = root_node
        if current is None:
            return
        self.nodes_counter += 1
        self.count(current.left_child)
        self.count(current.right_child)
        return self.nodes_counter

    def __str__(self):
        def append_r(node, level):
            s = ""
            if node is not None:
                s += append_r(node.right_child, level+1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += append_r(node.left_child, level+1)
            return s
        return append_r(self.root_node, 0)

def generate_data(max_value):
    """generates numbers from 1 up to a specified maximum"""
    count = 1
    while count <= max_value:
        yield count
        count += 1
l = list(generate_data(100))
random.shuffle(l)

def demo():
    t = Tree()
    for el in l:
        t.insert(el)
    print(t)
    print(f'item found, number of steps: {t.search(100)}')
    print(f'number of nodes: {t.count(t.root_node)}')
demo()