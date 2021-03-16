class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def __iter__(self):
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __str__(self):
        return "<-".join(str(item) for item in self)

    def empty(self):
        return len(self) == 0

    def peek(self):
        if not self.linked_list.head:
            return None
        return self.linked_list.head.data

    def enqueue(self, value):
        node = Node(value)
        if self.empty():
            self.front = self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        if self.empty():
            return None
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return node.data

    def clear(self):
        self.front = None
        self.back = None


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.dequeue()
    print(q)
