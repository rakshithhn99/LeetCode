class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       freq1 = [0] * 26 
       freq2 = [0] * 26 

       for i in s:
           freq1[ord(i) - ord('a')]+=1 
           
       for i in t:
            freq2[ord(i) - ord('a')]+=1 
        
       if freq1 == freq2:
            return True 
        
       return False


        