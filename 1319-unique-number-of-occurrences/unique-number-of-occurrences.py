class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for val in arr:
            if freq.get(val):
                freq[val]+=1
            else:
                freq[val] = 1

        final_freq = set()
        for key,values in freq.items():
            if values in final_freq:
                return False
            final_freq.add(values)
        
        return True
        