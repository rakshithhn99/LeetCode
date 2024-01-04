class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums) 
        
        insert = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[insert-2]:
                nums[insert] = nums[i] 
                insert+=1 
        
        return insert 
        


        