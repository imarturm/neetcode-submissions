class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        seen = set([0])
        queue = deque([(0, None)])
        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                seen.add(neighbor)
                queue.append((neighbor, node))

        return len(seen) == n