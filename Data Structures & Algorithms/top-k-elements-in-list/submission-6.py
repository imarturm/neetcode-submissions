import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            buckets[c].append(n)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            while buckets[i] and k > 0:
                res.append(buckets[i].pop())
                k -= 1
        return res