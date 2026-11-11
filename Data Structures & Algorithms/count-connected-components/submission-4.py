class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        size = [1] * n

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)

            if par1 == par2:
                return 0
            
            if size[par1] > size[par2]:
                par[par2] = par1
                size[par1] += size[par2]
            else:
                par[par1] = par2
                size[par2] += size[par1]
            return 1
        
        count = n
        for node1, node2 in edges:
            count -= union(node1, node2)
        return count