"""https://www.askpython.com/python/examples/avl-tree-in-python"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class Tree(object):
    def avl_height(self, root):
        if not root:
            return 0
        return root.height

    def avl_balance_factor(self, root):
        """calculates the balance factor of the node"""
        if not root:
            return 0
        return self.avl_height(root.left) - self.avl_height(root.right)

    def avl_min_value(self, root):
        """finds an empty node"""
        if root is None or root.left is None:
            return root
        return self.avl_min_value(root.left)

    def pre_order(self, root):
        """traverses the tree in a preorder way"""
        if not root:
            return
        print("{0} ".format(root.value), end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def left_rotate(self, b):
        a = b.right
        T2 = a.left
        a.left = b
        b.right = T2
        b.height = 1 + max(self.avl_height(b.left),
                           self.avl_height(b.right))
        a.height = 1 + max(self.avl_height(a.left),
                           self.avl_height(a.right))
        return a

    def right_rotate(self, b):
        a = b.left
        T3 = a.right
        a.right = b
        b.left = T3
        b.height = 1 + max(self.avl_height(b.left),
                           self.avl_height(b.right))
        a.height = 1 + max(self.avl_height(a.left),
                           self.avl_height(a.right))
        return a

    def insert_node(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.avl_height(root.left),
                              self.avl_height(root.right))

        # update the balance factor and balance the tree
        balanceFactor = self.avl_balance_factor(root)
        if balanceFactor > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balanceFactor < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete_node(self, root, value):
        """finds the node to be deleted and removes it"""
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete_node(root.left, value)
        elif value > root.value:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.avl_min_value(root.right)
            root.value = temp.key
            root.right = self.delete_node(root.right, temp.value)
        if root is None:
            return root

        # update the balance factor of nodes
        root.height = 1 + max(self.avl_height(root.left), self.avl_height(root.right))
        balanceFactor = self.avl_balance_factor(root)

        # balance the tree
        if balanceFactor > 1:
            if self.avl_balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balanceFactor < -1:
            if self.avl_balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def __str__(self, root=0):
        def append_r(node, level):
            s = ""
            if node is not None:
                s += append_r(node.right, level+1)
                s += "| " * level
                s += str(node.value) + "\n"
                s += append_r(node.left, level+1)
            return s
        return append_r(root, 0)

def demo():
    t = Tree()
    root = None
    root = t.insert_node(root, 40)
    root = t.insert_node(root, 60)
    root = t.insert_node(root, 50)
    root = t.insert_node(root, 80)
    root = t.insert_node(root, 70)
    root = t.insert_node(root, 90)

    print(t.__str__(root))

    print("PREORDER")
    t.pre_order(root)

demo()