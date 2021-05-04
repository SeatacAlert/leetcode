#我的解
#因为是求最短距离，所以必须是BFS
#因为可以来回跳，所以DP不行，必须是BFS
#这里要注意每次使用完，del pos[arr[start]] ，防止重复访问
from queue import Queue
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = set([0])
        s = set()
        s.add(0)
        pos = {}
        for i, value in enumerate(arr):
            if value not in pos:
                pos[value] = set()
            pos[value].add(i)
        dp = [-1] * len(arr)
        dp[0] = 0
        while q:
            qq = set()
            for start in q:
                if start-1>=0 and dp[start-1] == -1:
                    dp[start-1] = dp[start] + 1
                    qq.add(start-1)
                if start+1<len(arr) and dp[start+1] == -1:
                    qq.add(start+1)
                    dp[start+1] = dp[start] + 1
                if arr[start] in pos:
                    for other in pos[arr[start]]:
                        if dp[other] == -1:
                            qq.add(other)
                            dp[other] = dp[start] + 1
                    del pos[arr[start]]
            q = qq
        return dp[len(arr) - 1]
            
        
            

#最快解
#它做了一个优化：# Ignore center of 3+ consecutive equal values
#连续相等的值，只留两端，中间的值全部忽略，这个优化不错

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if n == 2:
            return 1
        if arr[0] == arr[n - 1]:
            return 1
        if n == 3 or arr[0] == arr[n - 2] or arr[1] == arr[n - 1]:
            return 2

        dist = [-1] * n
        dist[0] = 0

        value_to_indices = {arr[n - 1]: [n-1]}
        last = arr[0]+1
        for j, x in enumerate(arr[:-1]):
            if x not in value_to_indices:
                value_to_indices[x] = [j]
            # Ignore center of 3+ consecutive equal values
            elif x == last == arr[j + 1]:
                dist[j] = -2
                continue
            else:
                value_to_indices[x].append(j)
            last = x

        # All unique values = all steps of size 1
        if len(value_to_indices) == n:
            return n - 1

        to_visit = [0]
        # BFS
        for curr_ind in to_visit:
            curr_dist = dist[curr_ind]

            if curr_ind == n - 1:
                return curr_dist
            if curr_ind == n-2:
                return curr_dist+1

            val = arr[curr_ind]
            if val in value_to_indices:
                values = value_to_indices.pop(val)
                for new_ind in values:
                    if dist[new_ind] == -1:

                        dist[new_ind] = curr_dist + 1
                        if new_ind == n - 1:
                            return curr_dist + 1
                        to_visit.append(new_ind)

            if curr_ind != 0 and dist[curr_ind - 1] == -1:
                dist[curr_ind - 1] = curr_dist + 1
                to_visit.append(curr_ind - 1)

            if dist[curr_ind + 1] == -1:
                dist[curr_ind + 1] = curr_dist + 1
                to_visit.append(curr_ind + 1)
