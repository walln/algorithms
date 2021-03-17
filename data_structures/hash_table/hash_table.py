class HashTable:
    def __init__(self, size=50):
        self.size = size
        self.table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set(self, key, val):
        hkey = hash(key) % self.size
        bucket = self.table[hkey]
        found = False
        for index, record in enumerate(bucket):
            k, _ = record
            if k == key:
                found = True
                break

        if found:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get(self, key):
        hkey = hash(key) % self.size
        bucket = self.table[hkey]
        found = False
        for index, record in enumerate(bucket):
            k, v = record
            if k == key:
                found = True
                break
        if found:
            return v
        else:
            return None

    def delete(self, key):
        hkey = hash(key) % self.size
        bucket = self.table[hkey]
        found = False
        for index, record in enumerate(bucket):
            k, _ = record
            if k == key:
                found = True
                break
        if found:
            bucket.pop(index)
        return

    def keys(self):
        keys = []
        for item in self.table:
            if item != []:
                for pair in item:
                    key, _ = pair
                    keys.append(key)
        return keys

    def values(self):
        values = []
        for item in self.table:
            if item != []:
                for pair in item:
                    _, value = pair
                    values.append(value)
        return values

    def __str__(self):
        return (
            "".join(str(item) for item in self.table if item != [])
            .replace("[", "")
            .replace("]", ", ")
        )[:-2]


if __name__ == "__main__":
    ht = HashTable()
    ht.set("test", "1")
    ht.set("test2", "2")
    print(ht)
    print(ht.keys())
    print(ht.values())
    print(ht.get("test"))
    ht.delete("test2")
    print(ht)
    print(ht.keys())
    print(ht.values())

    ht2 = HashTable()
    for x in range(51):
        ht2.set(x, x)
    print(ht2)
