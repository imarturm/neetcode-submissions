class PrefixTree:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        cur = self.children
        for c in word:
            cur.setdefault(c, {})
            cur = cur[c]
        cur["END"] = True

    def search(self, word: str) -> bool:
        cur = self.children
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "END" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.children
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True
        