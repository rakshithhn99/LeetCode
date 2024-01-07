# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(1):
            return 1

        low = 1; high = n
        while low <= high:
            mid = low+(high-low) // 2
            status = isBadVersion(mid)

            if not status:
                if isBadVersion(mid+1):
                    return mid+1
                low = mid+1 

            if status:
                if not isBadVersion(mid-1):
                    return mid 
                high = mid-1
            
            
        