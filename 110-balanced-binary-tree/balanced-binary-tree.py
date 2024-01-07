# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def heightandbalance(root):
            if root is None:
                return [0, True]
            
            left = heightandbalance(root.left)
            right = heightandbalance(root.right)

            balance = (left[1] and right[1] and abs(left[0] - right[0]) <=1)
            print(balance) 

            return [1 + max(left[0], right[0]), balance]

        return heightandbalance(root)[1]


        