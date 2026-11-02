class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for ring in range((n + 1) // 2):
            for offset in range(n - 1 - (2 * ring)):
                top = matrix[ring][ring + offset]
                matrix[ring][ring + offset] = matrix[n - ring - offset - 1][ring]
                matrix[n - ring - offset - 1][ring] = matrix[n - ring - 1][n - ring - offset - 1]
                matrix[n - ring - 1][n - ring - offset - 1] = matrix[ring + offset][n - ring - 1]
                matrix[ring + offset][n - ring - 1] = top
                