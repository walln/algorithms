class Trie:
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert(self, word):
        current = self
        for c in word:
            if c not in current.nodes:
                current.nodes[c] = Trie()
            current = current.nodes[c]
        current.is_leaf = True

    def find(self, word):
        current = self
        for c in word:
            if c not in current.nodes:
                return False
            current = current.nodes[c]
        return current.is_leaf

    def delete(self, word):
        def __delete__(current, word, index):
            if index == len(word):
                if not current.is_leaf:
                    return False
                current.is_leaf = False
                return len(current.nodes) == 0
            c = word[index]
            c_node = current.nodes.get(c)
            if not c_node:
                return False
            delete = __delete__(c_node, word, index + 1)
            if delete:
                del current.nodes[c]
                return len(current.nodes) == 0
            return delete

        __delete__(self, word, 0)

    def display(self):
        def __print__(node, word=""):
            if node.is_leaf:
                print(word, end=" ")
            for key, value in node.nodes.items():
                __print__(value, word + key)

        __print__(self)


if __name__ == "__main__":
    t = Trie()
    words = "apple apples ace ampersand australia adverse purple".split()
    for word in words:
        t.insert(word)

    t.display()

    assert t.find("apple")
    assert t.find("apples")
    assert t.find("ace")
    assert not t.find("aces")
    t.delete("apple")
    assert not t.find("apple")
    assert t.find("apples")