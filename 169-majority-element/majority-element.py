class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        interval = n // 2
        i = 0
        while i + interval < n:
            if nums[i] == nums[i+interval]:
                break
            i+=1 
        
        return nums[i]
        