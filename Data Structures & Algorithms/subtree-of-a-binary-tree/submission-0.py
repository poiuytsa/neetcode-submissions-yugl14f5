# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
        self.same=False
        def dfs(node):
            if not node:
                return None
            if not self.same:
                self.same=sameTree(node,subRoot)
            dfs(node.left) 
            dfs(node.right)

        dfs(root)
        return self.same