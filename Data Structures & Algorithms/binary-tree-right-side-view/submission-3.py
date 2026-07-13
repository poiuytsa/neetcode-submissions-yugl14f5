# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs=[]
        q=deque([root])
        if not root:
            return []
        while q:
            lvl=[]
            for i in range(len(q)):
                node=q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            bfs.append(lvl)
        
        print(bfs)

        res=[]
        for n in bfs:
            res.append(n[-1])

        return res