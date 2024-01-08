class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 256
        for i in s:
            freq[ord(i)]+=1 
        
        longPal = 0; oddLength = False
        for i, index in enumerate(freq):
            if freq[i] % 2:
                longPal += (freq[i]-1)
                oddLength = True 
                continue 

            longPal+= freq[i]

        if oddLength:
            return longPal+1
        return longPal
            
                
        