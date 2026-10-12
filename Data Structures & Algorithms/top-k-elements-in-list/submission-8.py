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
        for c in range(len(buckets) - 1, 0, -1):
            for n in buckets[c]:
                res.append(n)
                if len(res) == k:
                    return res