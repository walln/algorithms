from pprint import pformat


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def __printtree__(self):
        if self.left:
            self.left.__printtree__()
        print(self.data)
        if self.right:
            self.right.__printtree__()

    def preorder(self):
        res = []
        res.append(self.data)
        if self.left:
            res = res + self.left.preorder()
        if self.right:
            res = res + self.right.preorder()
        return res

    def inorder(self):
        res = []
        if self.left:
            res = res + self.left.inorder()
        res.append(self.data)
        if self.right:
            res = res + self.right.inorder()
        return res

    def postorder(self):
        res = []
        if self.left:
            res = res + self.left.inorder()
        if self.right:
            res = res + self.right.inorder()
        res.append(self.data)
        return res


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)

    def empty(self):
        return self.root is None

    def insert(self, val):
        if self.root is not None:
            self.root.insert(val)
        else:
            self.root = Node(val)

    def preorder(self):
        return self.root.preorder()

    def inorder(self):
        return self.root.inorder()

    def postorder(self):
        return self.root.postorder()


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(3)
    bt.insert(2)
    bt.insert(7)

    print(bt.preorder())
    print(bt.inorder())
    print(bt.postorder())