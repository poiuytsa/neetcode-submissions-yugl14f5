class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)

        def find(x):
            if par[x]==x:
                return par[x]
            par[x]=find(par[x])
            return par[x]

        def union(a,b):
            pa,pb=find(a),find(b)

            if pa==pb:
                return False

            if rank[pa]<rank[pb]:
                par[pa]=pb
                rank[pb]+=rank[pa]
            else:
                par[pb]=pa
                rank[pa]+=rank[pb]

            return True

        for u,v in edges: 
            if not union(u,v): 
                return [u,v]