class Queue:
    def __init__(self):
        self.elems = []

    def enqueue(self, data):
        self.elems.append(data)

    def dequeue(self):
        pop = self.elems[0]
        self.elems = self.elems[1:]
        return pop

    def peek(self):
        return self.elems[0]

    def __len__(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)


if __name__ == "__main__":
    q = Queue()
    for x in range(6):
        q.enqueue(x)
    print(q)
    q.dequeue()
    print(q)