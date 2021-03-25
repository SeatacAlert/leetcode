class Solution: # beat 93% [i,j]
    def balancedString(self, s: str) -> int:
        c = Counter(list(s))
        L = len(s)
        need = 4
        for key in "QWER":
            c[key] = L//4 - c[key]
            if c[key] >= 0:
                need -= 1
        
        if need == 0:
            return 0

        minv = float('inf')
        i = 0
        for j, chj in enumerate(s):
            c[chj] += 1
            if c[chj] == 0:
                need -= 1
            while need == 0 and i < j+1:
                if c[s[i]] == 0:
                    minv = min(minv, j+1 - i)
                    need += 1
                c[s[i]] -= 1    
                i += 1
        return minv
    
    """
    class Solution:
    def balancedString(self, s: str) -> int:
        avgl = len(s)//4
        count = collections.Counter(s)
        d = collections.defaultdict(int)
        for x in ['Q', 'W', 'E', 'R']:
            if count[x] - avgl > 0:
                d[x] = count[x] - avgl
            
        res = float('inf')
        l, r = 0, 0
        c = len(d)
        if c == 0:
            return 0
        
        while r < len(s):
            ch = s[r]
            if ch in d:
                d[ch] -= 1
                if d[ch] == 0:
                    c -= 1
            r += 1
            while c == 0:
                res = min(res, r - l)
                ch = s[l]
                if ch in d:
                    d[ch] += 1
                    if d[ch] > 0:
                        c += 1
                l += 1
        return res
    """
