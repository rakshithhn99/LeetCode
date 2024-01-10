class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        def reverseArrayRange(arr, left, right):
            while left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1
        
        reverseArrayRange(nums, n-k, n-1)
        reverseArrayRange(nums, 0, n-k-1)
        reverseArrayRange(nums, 0, n-1)
        


        