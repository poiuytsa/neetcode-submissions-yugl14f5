"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None 

        mapping={}
        visited=set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            mapping[node]=Node(node.val)
            for n in node.neighbors:
                dfs(n)
        dfs(node)
        

        visited2=set()
        def dfs2(node):
            if node in visited2:
                return
            visited2.add(node)
            for n in node.neighbors:
                mapping[node].neighbors.append(mapping[n])
            for n in node.neighbors:
                dfs2(n)
        
        dfs2(node)

        return mapping[node] 