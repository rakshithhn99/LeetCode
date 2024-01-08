class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) 
        if n == 0 or n == 1:
            return n
        
        freq = [0] * 256
        left = 0; right=0; max_len = 1
        while right < n and left<=right:
            if not freq[ord(s[right])]:
                freq[ord(s[right])]+=1
                right+=1
                continue

            
            max_len = max(max_len, right-left)
            freq[ord(s[left])]-=1
            left+=1
        
        max_len = max(max_len, right-left)
        return max_len





        