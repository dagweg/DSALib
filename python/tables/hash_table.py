class HashTable:
    def __init__(self, elements=[]):
        N = len(elements)
        self.arr = [None for _ in range(N)]
        for i in range(N):
            if self.arr[self.hash(elements[i])] is not None:
                if not isinstance(self.arr[self.hash(elements[i])], list):
                    self.arr[self.hash(elements[i])] = [self.arr[self.hash(elements[i])]]
                self.arr[self.hash(elements[i])].append(elements[i])
            else:
                self.arr[self.hash(elements[i])] = elements[i]

    def hash(self, element):
        if isinstance(element, int):
            return element % len(self.arr)
        elif isinstance(element, str):
            temp = 0
            for c in element:
                temp += ord(c)
            return temp % len(self.arr)

    def get(self, element):
        return self.arr[self.hash(element)]

    def set(self, element, value):
        self.arr[self.hash(element)] = value

    def pop(self, element):
        slot = self.hash(element)
        if isinstance(self.arr[slot], list):
            self.arr[slot].remove(element)
            if len(self.arr[slot]) == 0:
                self.arr[slot] = None
        else:
            self.arr[slot] = None


if __name__ == "__main__":
    hash_table = HashTable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(hash_table.get(3))
    hash_table.pop(3)
    print(hash_table.get(3))
    hash_table.set(4, 3)
    print(hash_table.get(4))
