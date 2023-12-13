# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None :
            return False
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
            else:
                return False
        
        stack = [root]; visited = []; traverselist = []
        while stack:
            top = stack[len(stack)-1]
            if top in visited:
                stack.pop()
                traverselist.pop()
                visited.remove(top)
                continue

            visited.append(top)
            traverselist.append(top.val)

            if top.left is None and top.right is None and sum(traverselist) == targetSum:
                return True
            
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)    

        return False