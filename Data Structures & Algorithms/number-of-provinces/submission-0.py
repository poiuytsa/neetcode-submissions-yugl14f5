class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=[[] for i in range(len(isConnected))]

        for i,n in enumerate(isConnected):
            for j,nei in enumerate(n):
                if nei and j!=i:
                    adj[i].append(j)

        print(adj)

        visited=set()
        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)
        
        res=0
        for i in range(len(isConnected)):
            if i not in visited:
                print(visited)
                dfs(i)
                res+=1 

        return res
