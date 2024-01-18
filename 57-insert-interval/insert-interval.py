class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i=0
        while i < len(intervals):
            if newInterval[0] <= intervals[i][0]:
                if newInterval[0] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                else:
                    intervals.insert(i+1, newInterval)
                break
            
            i+=1
        
        if i == len(intervals):
            intervals.append(newInterval)

        print(intervals)
        
        first = intervals[0][0]
        second = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= first and intervals[i][0] <= second:
                second = max(second, intervals[i][1])
                continue 
            result.append([first,second])
            first = intervals[i][0]
            second = intervals[i][1]

        result.append([first,second])
        return result
            

        