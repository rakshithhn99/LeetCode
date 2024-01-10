class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        #go with concept left and right sum by excluding current value
        rightSum = total; leftSum = 0; n = len(nums)
        res = [0]*len(nums)

        for index,value in enumerate(nums):
            rightSum-=value
            leftMul = value * (index-0)
            rightMul = value * (n-1-index)
            
            res[index] = (leftMul - leftSum) + (rightSum - rightMul)
            leftSum+=value 

        return res

        