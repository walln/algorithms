class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def contains(self, val):
        return val in self.stack

    def empty(self):
        return len(self.stack) != 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(5)
    s.push(3)

    print(s)
    s.pop()
    print(s)