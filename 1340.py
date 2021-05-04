#最快解,用stack
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr.append(math.inf)
        dp = [1] * len(arr)
        stack = [-1]
        for i, x in enumerate(arr):

            while arr[stack[-1]] < x:
                L = [stack.pop()]

                while arr[stack[-1]] == arr[L[0]]:
                    L.append(stack.pop())

                for j in L:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)

            stack.append(i)
        return max(dp[:-1])
      
      
#我的超慢解
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        seq = sorted([(v,i) for i, v in enumerate(arr)])
        dp = [0] * len(arr)
        res = 0
        for v, i in seq:
            cur = 0
            cur1 = 0
            for direction in (1, -1):
                for d2 in range(1,d+1):
                    d1 = direction * d2
                    cur1 = 0
                    if 0 <= i+d1 and i+d1 < len(arr) and arr[i+d1] < v:
                        if arr[i+d1] > cur1:
                            cur = max(cur, dp[i+d1])
                            cur1 = max(cur1, arr[i+d1])            
                    else:
                        break

            dp[i] = cur + 1
            res = max(res, dp[i])
        return res
