class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        return "->".join([str(item) for item in self])

    def push_front(self, value):
        new_node = Node(value, self.head)
        this.head.prev = new_node
        this.head = new_node
        if self.tail is None:
            self.tail = new_node

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, value):
        if not self.head:
            return None
        node = self.head
        while node:
            if node.data == value:
                return node
            node = node.next
        return None

    def delete_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        node = self.tail
        node.prev.next = None

    def delete_head(self):
        if not self.head:
            return None
        deleted = self.head
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        return deleted

    def delete(self, value):
        node = self.head
        while node.data != value:
            if node.next:
                node = node.next
            else:
                return None
        if node == self.head:
            self.delete_head()
        elif node == self.tail:
            self.delete_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return value

    def insert_many(self, *values):
        for value in values:
            self.push(value)

    def contains(self, value):
        node = self.head
        while node:
            if node.data == value:
                return True
            node = node.next
        return False

    def reverse(self):
        node = self.head
        prev_node = None
        next_node = None
        while node:
            next_node = node.next
            node.next = prev_node

            prev_node = node
            node = next_node
        self.tail = self.head
        self.head = prev_node

    def empty(self):
        return not self.head


if __name__ == "__main__":
    l = LinkedList()
    l.insert_many(1, 2, 3, 4, 4, 4, 5, 6)
    print(l)
    l.delete_tail()
    print(l)
    l.delete_head()
    print(l)
    l.delete(4)
    print(l)
    print(l.contains(4))
    while l.contains(4):
        l.delete(4)
    print(l)
    l.reverse()
    print(l)
    print(l.empty())
    print(l.find(3))
