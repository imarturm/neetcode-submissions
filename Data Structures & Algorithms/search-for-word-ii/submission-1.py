class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                cur = cur.setdefault(c, {})
            cur["END"] = True

        R, C = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        words_found = []
        current_word = []

        def dfs(cur, r, c):
            val = board[r][c]
            if val not in cur:
                return
            
            board[r][c] = "#"
            current_word.append(val)
            cur = cur[val]
            if cur.pop("END", None):
                words_found.append("".join(current_word))
            
            for dr, dc in directions:
                if r + dr in range(R) and c + dc in range(C):
                    dfs(cur, r + dr, c + dc)
            
            board[r][c] = val
            current_word.pop()

        for r in range(R):
            for c in range(C):
                dfs(trie, r, c)
        return words_found