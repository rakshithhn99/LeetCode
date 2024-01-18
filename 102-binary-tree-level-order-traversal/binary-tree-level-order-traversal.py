# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []; queue = [[root]]
        while queue:
            front = queue.pop(0)
            temp = []
            temp_res = []
            for node in front:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                
                temp_res.append(node.val)
            if temp:
                queue.append(temp)
            
            if temp_res:
                res.append(temp_res)

        return res


      