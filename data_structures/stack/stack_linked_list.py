class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        out = []
        node = self.head
        while node:
            out.insert(0, node.data)
            node = node.next
        return str(out)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            return temp

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head

    def empty(self):
        return self.head is None

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    s.pop()
    print(s)