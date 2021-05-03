#这是我的解：
#
#对每个点(x,y)，它存在四个象限的角 [(-1,-1), (-1,1), (1,-1), (1,1)]
#当邻角比如(-1,-1),(-1,1)这种相邻角出现时，这个点必定在边上，或内部，必定不是顶点。
#当出现三个角时，这个点是一个内部顶点，凹点。
#当四个角都出现时，这个点是一个内部点
#当两个相同角出现时，这个点处出现了重叠
#
#对于一个图形，它的外轮廓至少有4个顶点（因为是矩形组成的）
#也就至少有4个单点 （不成对的点）
#如果出现了重叠，那么将最外面的图像移除以后，还有图形，这个新图形也会有一个外轮廓，这个外轮廓也有至少4个单点
#但是这4个单点与之前的4个单点，只可能重复，不可能成对，如果成对，意味着新图形其实有一部分可以转移给旧图形，这与原图形是外轮廓是矛盾的。
#如果图像有空洞，那么内部也有单点
#
#总之，当我们统计顶点的时候，成对点一起去掉，最后统计剩下的单点数（注意不成对不能去掉）
#这个单点数是4即可。
#
#因为 左上和右下角 可以跟 左下和右上角 成对
#所以 左上和右下角 直接+1， 左下和右上角 直接-1，即可统计出不成对角的个数

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        angles = {}
        for x1,y1,x2,y2 in rectangles:
            if x1 > x2:
                x1,x2 = x2,x1
            if y1 > y2:
                y1,y2 = y2,y1
            angles[(x1,y1)] = angles.get((x1,y1), 0) + 1
            angles[(x2,y2)] = angles.get((x2,y2), 0) + 1
            angles[(x1,y2)] = angles.get((x1,y2), 0) - 1
            angles[(x2,y1)] = angles.get((x2,y1), 0) - 1
        x = 0
        for key in angles:
            x += abs(angles[key])
        return x == 4

# 下面这是最快解：
# 进行对称差的更新，即留下最终的单点，但是它统计单点的时候，不区分是哪个方向的角
# 然后增加面积
# 然后找出了最小点，即 x+y最小的点 和 x+y最大的点，这四个点可以求出总面积
# 这个方法是基于
# 条件1：单点只有4个
# 条件2：面积相等
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s, area = set(), 0
        for x1, y1, x2, y2 in rectangles:
            s.symmetric_difference_update({(x1, y1), (x1, y2), (x2, y1), (x2, y2)})
            area += (x2-x1) * (y2-y1)
        if len(s) != 4:
            return False
        x1, y1 = min(s, key = lambda a: a[0]+a[1])
        x2, y2 = max(s, key = lambda a: a[0]+a[1])
        return len(s) == 4 and area == (x2-x1) * (y2-y1)
