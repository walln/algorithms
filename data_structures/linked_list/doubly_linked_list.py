class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return " ".join(str(node) for node in nodes)

    def __contains__(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before_node(self.head, node)

    def set_tail(self, node):
        if self.head is None:
            self.set_head(node)
        else:
            self.insert_after_node(self.tail, node)

    def insert_before_node(self, node, insert_node):
        insert_node.next = node
        insert_node.prev = node.prev

        if node.prev is None:
            self.head = insert_node
        else:
            node.prev.next = insert_node

        node.prev = insert_node

    def insert_after_node(self, node, insert_node):
        insert_node.prev = node
        insert_node.next = node.next
        if node.next is None:
            self.tail = insert_node
        else:
            node.next.prev = insert_node

        node.next = insert_node

    def insert(self, val):
        node = Node(val)
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)

    def get(self, val):
        node = self.head
        while node:
            if node.data == val:
                return node
            node = node.next
        return None

    def empty(self):
        return self.head is None


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(5)

    print(dll)