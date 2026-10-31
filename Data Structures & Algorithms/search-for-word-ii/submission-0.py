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
        words_found = set()
        current_word = []

        def dfs(cur, r, c):
            if r not in range(R) or c not in range(C):
                return
            val = board[r][c]
            if val not in cur:
                return
            
            board[r][c] = "#"
            current_word.append(val)
            cur = cur[val]
            if "END" in cur:
                words_found.add("".join(current_word))
            for dr, dc in directions:
                dfs(cur, r + dr, c + dc)
            
            board[r][c] = val
            current_word.pop()

        for r in range(R):
            for c in range(C):
                dfs(trie, r, c)
        return list(words_found)