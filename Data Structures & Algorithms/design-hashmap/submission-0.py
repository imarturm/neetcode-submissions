class MyHashMap:

    def __init__(self):
        self.num_buckets = 1009
        self.buckets = [[] for _ in range(self.num_buckets)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % self.num_buckets]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])   

    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.num_buckets]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.num_buckets]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)