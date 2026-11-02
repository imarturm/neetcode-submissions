class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        rings = (min(m, n) + 1) / 2
        for ring in range(int(rings)):
            for c in range(n - (ring * 2)):
                res.append(matrix[ring][ring + c])
            for r in range(1, m - (ring * 2)):
                res.append(matrix[ring + r][-ring - 1])
            if ring == rings - 1:
                break
            for c in range(1, n - (ring * 2)):
                res.append(matrix[-ring - 1][-ring - 1 - c])
            for r in range(1, m - (ring * 2) - 1):
                res.append(matrix[-ring - 1 - r][ring])
        return res

        #[2 5 8]
        #[4 0 1]