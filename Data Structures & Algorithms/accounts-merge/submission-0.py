class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        size = [1] * n

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 != par2:
                if size[par1] > size[par2]:
                    par[par2] = par1
                    size[par1] += size[par2]
                    email_to_index[email] = par1
                else:
                    par[par1] = par2
                    size[par2] += size[par1]
                    email_to_index[email] = par2

        email_to_index = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(email_to_index[email], i)
                else:
                    email_to_index[email] = i
        
        index_to_emails = defaultdict(list)
        for email, i in email_to_index.items():
            leader = find(i)
            index_to_emails[leader].append(email)
        
        return [[accounts[i][0]] + index_to_emails[i] for i in index_to_emails.keys()]