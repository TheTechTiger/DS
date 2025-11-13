class HashTableChaining:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self.hash_function(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return True
        return False
# Driver code
ht = HashTableChaining()

# Insert some key-value pairs
ht.insert(5, "Apple")
ht.insert(15, "Banana")
ht.insert(25, "Orange")
ht.insert(35, "Grape")

# Search for values
print("Value for key 15:", ht.search(15))
print("Value for key 25:", ht.search(25))
print("Value for key 10:", ht.search(10))

# Delete some entries
print("Deleting key 15:", ht.delete(15))
print("Deleting key 10:", ht.delete(10))

# Verify deletion
print("Value for key 15 after deletion:", ht.search(15))