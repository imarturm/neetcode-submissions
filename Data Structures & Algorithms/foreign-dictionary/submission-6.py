class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}
        indeg = {c: 0 for word in words for c in word}

        # Build adj list
        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    adj[c1].append(c2)
                    indeg[c2] += 1
                    break

        # Topological sort
        order = []
        queue = deque(c for c in indeg if indeg[c] == 0)
        while queue:
            c = queue.popleft()
            order.append(c)
            for neighbor in adj[c]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
        return "".join(order) if len(order) == len(indeg) else ""