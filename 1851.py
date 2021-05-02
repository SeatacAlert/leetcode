#我的解
from heapq import heappop, heappush
from bisect import bisect_left
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        for i in range(len(intervals)):
            if (intervals[i][0] > intervals[i][1]):
                intervals[i] = [intervals[i][1], intervals[i][0]]
        intervals.sort()
        h = []
        points = []
        for i, j in intervals:
            points.append(i)
            points.append(j)
        points = sorted(list(set(points)))
        cache = {}
        cache_p = {}
        interval_pos = 0
        for i, p in enumerate(points):
            while interval_pos < len(intervals) and (intervals[interval_pos][0] <= p):
                a,b = intervals[interval_pos]
                heappush(h, (b-a+1, a, b))
                interval_pos += 1
            while h[0][2] < p:
                heappop(h)
            cache_p[p] = h[0][0]
            while i+1 < len(points) and len(h) > 0 and h[0][2] < points[i+1]:
                heappop(h)
            if len(h) == 0:
                cache[p] = -1
            else:
                cache[p] = h[0][0]
                
        res = []
        for q in queries:
            if q in cache_p:
                res.append(cache_p[q])
            else:
                ind = bisect_left(points, q)
                if (ind == 0) or (ind == len(points)):
                    res.append(-1)
                else:
                    res.append(cache[points[ind-1]])
        return res
