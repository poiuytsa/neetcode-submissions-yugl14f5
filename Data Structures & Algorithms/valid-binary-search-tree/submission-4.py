# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid=True
        def dfs(node,leftAllowed,rightAllowed):
            if not node:
                return None
            if self.isValid:    
                if not leftAllowed<node.val<rightAllowed:
                    self.isValid=False
            
            dfs(node.left,leftAllowed,node.val)
            dfs(node.right,node.val ,rightAllowed)
        
        dfs(root,float("-inf"),float("inf"))
        
        return self.isValid