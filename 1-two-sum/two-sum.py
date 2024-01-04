class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, value in enumerate(nums):
            remindex = hash.get(target - value)
            if remindex is not None and remindex != index:
                return [index, remindex]
            
            hash[value] = index 
        
        return []
        

