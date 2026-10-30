import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # stores big values
        self.max_heap = [] # stores little values, negative values

    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, num)
        else:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return -self.max_heap[0]