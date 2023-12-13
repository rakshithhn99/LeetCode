# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        result = []
        queue = [[root]]
        while queue:
            front = queue.pop(0)
            level = []
            sub_queue=[]
            for el in front:
                level.append(el.val)
                if el.left:
                    sub_queue.append(el.left)
                if el.right:
                    sub_queue.append(el.right)
            if sub_queue:
                queue.append(sub_queue)
            result.append(level)
            print(result)



        print(result[::-1])
        return result[::-1]


        