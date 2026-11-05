class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            while par[node] != node:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(n1, n2):
            par1, par2 = find(n1), find(n2)

            if par1 == par2:
                return 0
            
            if rank[par1] > rank[par2]:
                rank[par1] += rank[par2]
                par[par2] = par1
            else:
                rank[par2] += rank[par1]
                par[par1] = par2
            return 1
        
        res = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    res -= union(i, j)
        return res