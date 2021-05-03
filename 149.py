# 最快解
# 这里它的key只有斜率，这是因为既然最优解一定是在统计某个起点p1的时候就能得到的，那么没必要记录所有的直线，只需要记录斜率即可，然后针对下一个起点，重新统计，极大地节约了
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        result = 0
        n = len(points)
        
        for i in range(n):
            same_points = 1
            slop_map = {'inf': 0}
            xi, yi = points[i]
            
            for j in range(i+1, n):
                xj, yj = points[j]
                
                if xi == xj and yi == yj:
                    same_points += 1
                
                if xi == xj:
                    slop_map['inf'] += 1
                
                else:
                    slop = (yj - yi) / (xj - xi)
                    slop_map[slop] = slop_map.get(slop, 0) + 1
                    
            result = max(result, max(slop_map.values()) + same_points)
                
        
        return result
      
# 我的解比较傻：记录了所有的直线
# 而且为了不用小数，我使用了最大公约数，所以只击败了25%
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = {}
        if (len(points) <= 2):
            return len(points)
        def lcd(a, b):
            if a > b:
                a, b = b, a
            while (a != 0):
                a, b = b%a, a
            return b
        
        def simplify(a, b, c):
            x = lcd(a,b)
            y = lcd(a,c)
            z = lcd(x,y)
            return z
            
        for i, p1 in enumerate(points):
            x1, y1 = p1
            key = None
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if (x1 == x2):
                    key = ("x", x1)
                elif (y1 == y2):
                    key = ("y", y1)
                else:
                    p = simplify(x2-x1, y2-y1, x2*y1-x1*y2)
                    if (x2-x1 > 0):
                        p = -p
                    key = ((x2-x1)//p, (y2-y1)//p, (x2*y1-x1*y2)//p)
                if key not in lines:
                    lines[key] = set()
                lines[key].add((x1,y1))
                lines[key].add((x2,y2))
        
        max_points = 0
        for key in lines:
            if len(lines[key]) > max_points:
                max_points = len(lines[key])
        
        return max_points
        
        
