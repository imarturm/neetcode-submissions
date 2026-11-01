class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        res = 0
        seen = set()
        queue = deque()
        for i in range(n):
            if i in seen:
                continue
            res += 1
            seen.add(i)
            queue.append(i)
            while queue:
                for neighbor in adj[queue.popleft()]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
        return res