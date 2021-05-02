#我的答案：
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num1 = num
        for i in range(k):
            pos = len(num) - 1
            while num[pos] <= num[pos-1]:
                pos -= 1
            pos2 = len(num) - 1
            while num[pos2] <= num[pos-1]:
                pos2 -= 1
            newnum = ''.join(reversed(list(num[pos:pos2] + num[pos-1] + num[pos2+1:])))
            num = num[:pos-1] + num[pos2] + newnum
        return self.getdiff(num1, num)
    def getdiff(self, num1, num2):
        for i, ch in enumerate(num1):
            if num1[i] != num2[i]:
                j = i
                while num2[j] != num1[i]:
                    j+=1
                return j-i + self.getdiff(num1[i+1:], num2[i:j] + num2[j+1:])
        return 0

#下面是某位选手的答案
#(1)字符串的翻转，它的方法是 s[::-1]，这很巧妙
#(2)在生成next permutation的时候，它没有重新组装，而是采用替换的方式，
#l[i], l[j] = l[j], l[i]
#l[i + 1:] = l[i + 1:][::-1]
#(3)它始终使用pop进行元素删除, pop(0), pop(n), 但是注意这些操作的复杂度都是O(n)
#学习了正确使用pop的方法，但是其实这样时间复杂度比较高
#不如list_name.index(element, start, end)，不修改原列表
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

    
