class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) == 1:
            if s == t:
                return s
            else:
                return ""

        if len(t) > len(s):
            return ""
        
        l=0; r=0; n = len(s)
        hash_map = {}; track_map = {}; 
        min_length = 1000005; min_substr = ""

        for ch in t:
            if not hash_map.get(ch, None):
                hash_map[ch]=1 
            else:
                hash_map[ch]+=1

        def compareEqual(hash_map, track_map):
            for key in hash_map:
                if not track_map.get(key, None):
                    return False

                if track_map[key] < hash_map[key]:
                    return False 

            return True

        while l<=r and r<n:

            if compareEqual(hash_map, track_map):
                if min_length > (r-l):
                    min_length = (r-l)
                    min_substr = s[l:r]
                    print(min_substr)

                if hash_map.get(s[l], None):
                    track_map[s[l]]-=1
                l+=1
                continue 
            
            if hash_map.get(s[r], None):
                if not track_map.get(s[r], None):
                    track_map[s[r]]=1
                else:
                    track_map[s[r]]+=1 
            r+=1 
        
        while l<n and compareEqual(hash_map, track_map):
            if min_length > (r-l):
                min_length = (r-l)
                min_substr = s[l:r]
            
            if hash_map.get(s[l], None):
                    track_map[s[l]]-=1
                
            l+=1 
        
        return min_substr
            


        