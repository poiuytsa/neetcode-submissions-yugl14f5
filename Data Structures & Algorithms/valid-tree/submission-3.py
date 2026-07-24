class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=[[] for i in range(n)]

        if len(edges)!=n-1:
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        def dfs(n,parent):
            if n in visited:
                return False 
            visited.add(n)
            for nei in adj[n]:
                if nei==parent:
                    continue
                if not dfs(nei,n):
                    return False
            return True 
        if not dfs(0,-1):
            return False 
        return len(visited)==n
