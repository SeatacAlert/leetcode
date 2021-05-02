# 重点是 int(s) == num: return True 针对一种特殊情形，00000，
# 因为全是0的话，如果一位一位匹配，只匹配第一位就返回了，但是其实也可以完全匹配上。
class Solution(object):
    def check(self, s, num):
        if len(s) == 0:
            return False
        if int(s) == num:
            return True
        for i in range(1, len(s)):
            if num == int(s[:i]):
                return self.check(s[i:], num-1)
            
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)):
            if self.check(s[i:], int(s[:i])-1):
                return True
        return False
