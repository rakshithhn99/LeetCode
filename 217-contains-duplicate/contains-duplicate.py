class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            val = hash.get(num,0) + 1
            if val >= 2:
                return True 
            hash[num] = val 

        return False

        