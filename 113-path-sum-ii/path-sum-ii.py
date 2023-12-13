# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root is None :
            return []
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []
        
        result = []; stack = [root]; visited = []; traverselist = []
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
                print(traverselist)
                result.append(traverselist.copy())
                print(result)
            
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)    

        return result

            

        