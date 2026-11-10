class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = {0}
        queue = deque([(0, None)])
        while queue:
            node, prev = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor, node))
        return len(visited) == n