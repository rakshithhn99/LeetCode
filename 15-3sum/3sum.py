class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0; n = len(nums)
        res = []
        hash = set()
        while i< n-2:
            first = nums[i] 
            j = i+1; k = n-1 
            while j<k:
                val  = first + nums[j] + nums[k]
                if val == 0:
                    triplet = (first, nums[j], nums[k])
                    hash.add(triplet)
                    j+=1 
                    k-=1
                elif val < 0:
                    j+=1
                    
                else:
                    k-=1
            
            i+=1
        
        for triplet in hash:
            res.append(list(triplet))
        return res

        return res


            
        

        