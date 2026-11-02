class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    dr = -1
                    while r + dr >= 0 and matrix[r + dr][c] != 0:
                        matrix[r + dr][c] = "#"
                        dr -= 1
                    dr = 1
                    while r + dr < m and matrix[r + dr][c] != 0:
                        matrix[r + dr][c] = "#"
                        dr += 1
                    dc = -1
                    while c + dc >= 0 and matrix[r][c + dc] != 0:
                        matrix[r][c + dc] = "#"
                        dc -= 1
                    dc = 1
                    while c + dc < n and matrix[r][c + dc] != 0:
                        matrix[r][c + dc] = "#"
                        dc += 1
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0