class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = {}
        for index,i in enumerate(points):
            res[index] = sqrt((i[0]*i[0]) + (i[1]*i[1]))
        
        sorted_res = sorted(res.items(), key= lambda x: x[1])

        kclose = []

        for key, value in sorted_res[:k]:
            kclose.append(points[key])
        return kclose




        