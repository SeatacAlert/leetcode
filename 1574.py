from bisect import bisect_right
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        leftinc = 0
        while (leftinc + 1 < len(arr) and arr[leftinc] <= arr[leftinc + 1]):
            leftinc += 1
        rightinc = len(arr) - 1
        while (rightinc - 1 >= 0 and arr[rightinc - 1] <= arr[rightinc]):
            rightinc -= 1
        if (leftinc >= rightinc):
            return 0
        leftpos = bisect.bisect_right(arr[:leftinc+1], arr[rightinc])

        maxlen = leftpos + len(arr) - rightinc # 4 + 8 - 6 = 6
        while (leftpos <= leftinc and rightinc <= len(arr)):
            leftpos += 1
            while (rightinc < len(arr) and arr[rightinc] < arr[leftpos - 1]):
                rightinc += 1
            maxlen = max(maxlen, leftpos + len(arr) - rightinc)
    
        return len(arr) - maxlen
