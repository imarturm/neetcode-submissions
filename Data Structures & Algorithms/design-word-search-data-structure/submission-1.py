class WordDictionary:

    def __init__(self):
        self.children = {}

    def addWord(self, word: str) -> None:
        cur = self.children
        for c in word:
            cur = cur.setdefault(c, {})
        cur["END"] = True

    def search(self, word: str) -> bool:
        def nested_search(cur, i):
            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    return any(nested_search(child, j + 1) for key, child in cur.items() if key != "END")
                if char not in cur:
                    return False
                cur = cur[char]
            return "END" in cur
        return nested_search(self.children, 0)