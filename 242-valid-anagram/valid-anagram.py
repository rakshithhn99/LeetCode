class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in s:
            if ds.get(i) is None:
                ds[i] = 1
            else:
                ds[i] = ds[i]+1

        
        for i in t:
            if dt.get(i) is None:
                dt[i] = 1
            else:
             dt[i]=dt[i]+1 
        
        print(ds)
        print(dt)
        if ds == dt:
            return True 
        
        return False

        