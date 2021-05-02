#这里在生成next permutation的时候，它没有重新组装，而是采用替换的方式，
#l[i], l[j] = l[j], l[i]
#l[i + 1:] = l[i + 1:][::-1]
#而在第二部进行比较的时候，它始终使用pop进行元素删除
#使用pop(0)弹出第一个元素，然后用index寻找下标，然后用pop(p)弹出
#这个人的原地操作手法高超
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        l = list(num)
        o = list(num)
        n = len(l)
        for _ in range(k):
            for i in range(n - 2, -1, -1):
                if l[i] < l[i + 1]:
                    break
            for j in range(n - 1, -1, -1):
                if l[j] > l[i]:
                    break
            l[i], l[j] = l[j], l[i]
            l[i + 1:] = l[i + 1:][::-1]
        
        ans = 0
        for _ in range(n):
            if l[0] == o[0]:
                l.pop(0)
                o.pop(0)
            else:
                p = o.index(l[0])
                l.pop(0)
                o.pop(p)
                ans += p
        return ans
