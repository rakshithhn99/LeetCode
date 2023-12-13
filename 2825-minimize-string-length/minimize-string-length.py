class Solution:
    def minimizedStringLength(self, s: str) -> int:

        freq = [0]*(26)    
        for i in s:
            if not freq[ord(i)-ord('a')]:
                freq[ord(i)-ord('a')] = 1
        return sum(freq)
        