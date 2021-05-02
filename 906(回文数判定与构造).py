# https://leetcode.com/problems/super-palindromes/discuss/174835/tell-you-how-to-get-all-super-palindrome(detailed-explanation)
构造分为两步：第一步，遍历所有<10^9的回文数，第二步算他们的平方
第一步如何做？遍历所有回文数是要去构造它，而不是一个一个去看
每个回文数都会分为 左+中+右 三个部分
构造所有回文数的方法是，对于每个数x，以下11种即为全部回文数：xx,x0x,x1x,..,x9x

所以第一步，构造是这样的：
res = [1,2,3,4,5,6,7,8,9] # initial
for i in range(1,10000): # we only need at most four digits to consturct nine digits
    s1 = str(i) + str(i)[::-1]
    res.append(s1)
    for j in range(10):
        s2 = str(i) + str(j) + str(i)[::-1]
        res.append(s2)
        
所有回文数的种类只有：11* 10000 + 9 也就是说回文数是很少的，接下来第二部就很容易了，判定是否为回文数只需要看它是否与自己的逆相同即可

def isPalin(s):
    return s == s[::-1]

res = list(map(int, res))
res.sort()
ans = []
for val in res:
    s = str(val**2)
    if isPalin(s):
        ans.append(int(s))
print(ans)
