//对每个点(x,y)，它存在四个象限的角 [(-1,-1), (-1,1), (1,-1), (1,1)]
//当邻角比如(-1,-1),(-1,1)这种相邻角出现时，这个点必定在边上，或内部，必定不是顶点。
//当出现三个角时，这个点是一个内部顶点，凹点。
//当四个角都出现时，这个点是一个内部点
//当两个相同角出现时，这个点处出现了重叠
//
//对于一个图形，它的外轮廓至少有4个顶点（因为是矩形组成的）
//也就至少有4个单点 （不成对的点）
//如果出现了重叠，那么将最外面的图像移除以后，还有图形，这个新图形也会有一个外轮廓，这个外轮廓也有至少4个单点
//但是这4个单点与之前的4个单点，只可能重复，不可能成对，如果成对，意味着新图形其实有一部分可以转移给旧图形，这与原图形是外轮廓是矛盾的。
//如果图像有空洞，那么内部也有单点
//
//总之，当我们统计顶点的时候，成对点一起去掉，最后统计剩下的单点数（注意不成对不能去掉）
//这个单点数是4即可。

//The right answer must satisfy two conditions:
//the large rectangle area should be equal to the sum of small rectangles
//count of all the points should be even, and that of all the four corner points should be one
public boolean isRectangleCover(int[][] rectangles) {

        if (rectangles.length == 0 || rectangles[0].length == 0) return false;

        int x1 = Integer.MAX_VALUE;
        int x2 = Integer.MIN_VALUE;
        int y1 = Integer.MAX_VALUE;
        int y2 = Integer.MIN_VALUE;
        
        HashSet<String> set = new HashSet<String>();
        int area = 0;
        
        for (int[] rect : rectangles) {
            x1 = Math.min(rect[0], x1);
            y1 = Math.min(rect[1], y1);
            x2 = Math.max(rect[2], x2);
            y2 = Math.max(rect[3], y2);
            
            area += (rect[2] - rect[0]) * (rect[3] - rect[1]);
            
            String s1 = rect[0] + " " + rect[1];
            String s2 = rect[0] + " " + rect[3];
            String s3 = rect[2] + " " + rect[3];
            String s4 = rect[2] + " " + rect[1];
            
            if (!set.add(s1)) set.remove(s1);
            if (!set.add(s2)) set.remove(s2);
            if (!set.add(s3)) set.remove(s3);
            if (!set.add(s4)) set.remove(s4);
        }
        
        if (!set.contains(x1 + " " + y1) || !set.contains(x1 + " " + y2) || !set.contains(x2 + " " + y1) || !set.contains(x2 + " " + y2) || set.size() != 4) return false;
        
        return area == (x2-x1) * (y2-y1);
    }
