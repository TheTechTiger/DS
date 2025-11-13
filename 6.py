class HashTableLinearProbing:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.deleted = object()

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash_function(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None or self.table[probe] == self.deleted:
                self.table[probe] = key
                return
            elif self.table[probe] == key:
                # Key already present
                return

    def search(self, key):
        idx = self.hash_function(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                return False
            if self.table[probe] == key:
                return True
        return False

    def delete(self, key):
        idx = self.hash_function(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                return False
            if self.table[probe] == key:
                self.table[probe] = self.deleted
                return True
        return False

    def display(self):
        print(self.table)

if __name__ == "__main__":
    ht = HashTableLinearProbing()

    # Insert a set of keys
    for key in [5, 15, 25, 35, 3, 13]:
        ht.insert(key)

    print("After inserts:")
    ht.display()

    # Search for existing and non-existing keys
    for key in [15, 99, 3]:
        print(f"Search {key}: {ht.search(key)}")

    # Delete a key and attempt to delete a non-existing key
    print("Delete 15:", ht.delete(15))
    print("Delete 99:", ht.delete(99))

    print("After deletions:")
    ht.display()

    # Insert into slot freed by deletion
    ht.insert(99)
    print("After inserting 99:")
    ht.display()