# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def targetsumArray(self, arr, target):
        count = 0
        arraySum = sum(arr)
        if arraySum == target:
            count+=1
        excludeSum = 0
        for i in arr[:-1]:
            excludeSum+=i
            if arraySum-excludeSum == target:
                count+=1
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None :
            return 0
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return 1
            else:
                return 0
        
        globalCount=0; stack = [root]; visited = []; traverselist = []
        while stack:
            top = stack[len(stack)-1]
            if top in visited:
                stack.pop()
                traverselist.pop()
                visited.remove(top)
                continue

            visited.append(top)
            traverselist.append(top.val)

            globalCount+=self.targetsumArray(traverselist, targetSum)
            print(traverselist)

            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)    

        return globalCount