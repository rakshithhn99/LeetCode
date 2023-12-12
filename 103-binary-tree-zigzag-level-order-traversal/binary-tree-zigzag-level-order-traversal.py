# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        t_list = [root, '|']
        l_ele = []
        level = 0

        while len(t_list):
            #print(t_list)
            front = t_list.pop(0)
            #print(front)

            if front == '|':
                if level % 2:
                    l_ele.reverse()
                result.append(l_ele.copy())
                level+=1
                l_ele.clear()
                if len(t_list):
                    t_list.append('|')
            
            else:
                l_ele.append(front.val)
                #print(front.val)

                if front.left is not None:
                    t_list.append(front.left)

                if front.right is not None:
                    t_list.append(front.right)

        return result
        