# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = [] 
        res2 = []
        def dfs(root, res):
            if not root:
                return None
            if not root.left and not root.right:
                res.append(root.val)

            dfs(root.left, res)
            dfs(root.right, res)

            return None

        dfs(root1, res1)
        dfs(root2, res2)

        print(res1)
        print(res2)
        if res1 == res2:
            return True
        
        return False
