class MyHashSet:

    def __init__(self):
        self.num_buckets = 1009
        self.buckets = [[] for _ in range(self.num_buckets)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.buckets[key % self.num_buckets].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.buckets[key % self.num_buckets].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % self.num_buckets]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)