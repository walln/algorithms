class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return " ".join(str(node) for node in nodes)

    def insert(self, data):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.head = Node(data)

    def get(self, val):
        node = self.head
        while node:
            if node.data == val:
                return node
            node = node.next
        return None

    def empty(self, val):
        return self.head is None