import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    queue.append((time + n, c))
            else:
                time = queue[0][0]
            if queue and queue[0][0] == time:
                heapq.heappush(heap, queue.popleft()[1])
        return time