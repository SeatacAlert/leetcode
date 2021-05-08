# 我的解，沿用了之前学过的方法，构造回文数，只需前半部分，然后对称复制
# 先添加两个基本候选，假设n是l位数，那么L+1位的最小数和L-1位的最大数当然是候选
# 接下来研究L位的比n大的最小数和比n小的最大数，
# 偶数位的话，就x[:l//2]一半，加1，减1
# 奇数位的话，中间数，加1，减1，但是也有特殊情况，如果中间数是9，那么加1以后进位，所以前半部分要+1，如果中间数是0，减1以后要借位，那么前半部分要减1
# 最后把所有的候选过一遍，不能等于原数，因为9999这种可能跟原数相等 
# 即可
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        num = int(n)
        candidates = []
        candidates.append(10 ** l + 1)
        candidates.append(10 ** (l-1) - 1)
        if l % 2 == 0:
            x = int(n[:l//2])
            candidates.append(int(str(x) + str(x)[::-1]))
            candidates.append(int(str(x+1) + str(x+1)[::-1]))
            candidates.append(int(str(x-1) + str(x-1)[::-1]))
        elif l > 1:
            x = int(n[:l//2])
            p = int(n[l//2])
            candidates.append(int(str(x) + str(p) + str(x)[::-1]))
            y = x + (p == 9)
            candidates.append(int(str(y) + str((p+1)%10) + str(y)[::-1]))
            y = x - (p == 0)
            candidates.append(int(str(y) + str((p-1)%10) + str(y)[::-1]))
        else:
            if int(n) > 0:
                candidates.append(int(n) - 1)
            if int(n) < 9:
                candidates.append(int(n) + 1)
            
        k = float(inf)
        for candidate in candidates:
            if candidate == num:
                continue
            if abs(candidate - num) < abs(k - num) or (abs(candidate - num) == abs(k - num) and candidate < k):
                k = candidate
        return str(k)
                            
# 这是最短最快解，跟我的差不多

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        maxLen, N = len(n), int(n)
        # Calculate bounds first.
        low, high = 10 ** (maxLen - 1) - 1, 10 ** maxLen + 1
        # Calculate remaining candidates.
        isOddLen = maxLen & 1
        firstHalf = int(n[:maxLen//2 + isOddLen])
        smaller = int(str(firstHalf - 1) + (str(firstHalf - 1)[::-1][1:] if isOddLen else str(firstHalf - 1)[::-1]))
        same = int(str(firstHalf) + (str(firstHalf)[::-1][1:] if isOddLen else str(firstHalf)[::-1]))
        larger = int(str(firstHalf + 1) + (str(firstHalf + 1)[::-1][1:] if isOddLen else str(firstHalf + 1)[::-1]))
        # Compare all the above results.
        if same == N:  # n is already a palindrome.
            return str(min(
                [low, high, smaller, larger],
                key=lambda x: (abs(x - N), x)))
        else:
            return str(min(
                [low, high, smaller, same, larger],
                key=lambda x: (abs(x - N), x)))
            
            
                            
                
            
            
