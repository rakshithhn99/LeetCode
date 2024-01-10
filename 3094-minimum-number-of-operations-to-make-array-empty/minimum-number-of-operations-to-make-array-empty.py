class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash = {}

        for el in nums:
            if not hash.get(el):
                hash[el] = 1
                continue 
            hash[el]+=1
        
        minOp = 0 
        print(hash)
        for key,value in hash.items():

            if value % 3 == 1 and value > 1:
                prev = (value // 3) - 1
                minOp+= prev
                value = value - (prev*3)

            if value % 3 !=1:
                minOp+= (value // 3)
                value = value % 3
            
            if value % 2 == 1:
                return -1 

            minOp+= (value // 2)
            value = value % 2
            print(value)
            
        return minOp
            
        