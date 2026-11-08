class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        indeg = {c: 0 for c in adj}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indeg[c2] += 1
                    break

        ordering = []
        queue = deque(c for c, i in indeg.items() if i == 0)
        while queue:
            c = queue.popleft()
            ordering.append(c)
            for neighbor in adj[c]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
        return "".join(ordering) if len(ordering) == len(indeg) else ""