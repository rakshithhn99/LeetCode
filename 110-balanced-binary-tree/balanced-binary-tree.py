# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def HeightBalanced(root):
            if not root:
                return [0, True]

            left_sub = HeightBalanced(root.left)
            right_sub = HeightBalanced(root.right)

            height = max(left_sub[0], right_sub[0]) + 1

            if abs(left_sub[0]-right_sub[0]) > 1 or not left_sub[1] or not right_sub[1]:
                return [height, False]
            
            return [height, True]
    
        return HeightBalanced(root)[1]
        