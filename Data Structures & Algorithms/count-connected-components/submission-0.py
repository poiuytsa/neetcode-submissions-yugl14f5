class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        def dfs(n):
            if n in visited:
                return  
            visited.add(n)
            for nei in adj[n]:
                dfs(nei)
        res=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
                if len(visited)==n:
                    return res