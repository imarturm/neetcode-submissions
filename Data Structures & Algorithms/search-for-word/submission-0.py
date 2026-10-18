class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r not in range(R) or c not in range(C) or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            found = any(dfs(r + d[0], c + d[1], i + 1) for d in directions)
            board[r][c] = word[i]
            return found
        return any(dfs(r, c, 0) for r in range(R) for c in range(C))