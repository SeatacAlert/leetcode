# 我的解
# 首先是如何判定两条线段是否相交
# 分为两种情况，相同方向，还是交叉方向
# 其次是通过试验我发现，它只会和最近的几条线段相交，这是因为它要么处于一个四方以内，要么处于一个四方以外，而这个四方是最近的几条线段。因此只需要判定是否与最近的几条线段相交即可。
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        def cross(x,y1,y2,y,x1,x2,i):
            if i == 0:
                return x1<=x and x<=x2 and y1<=y and y<=y2
            else:
                return x==y and not (y2 < x1 or x2 < y1)
        x, y = 0, 0
        q = []        
        for i, d in enumerate(distance):
            mod = i % 4
            if mod == 1:
                p = (x,y,y+d)
                y += d
            elif mod == 2:
                p = (y,x-d,x)
                x -= d 
            elif mod == 3:
                p = (x,y-d,y)
                y -= d 
            elif mod == 0:
                p = (y,x,x+d)
                x += d
            for index in range(1,6):
                if len(q) - index - 1 >= 0:
                    if cross(*p, *q[len(q) - index - 1], index % 2):
                        return True
            q.append(p)
        return False
