// 每个楼可能被左右两侧的楼限制(截断)。所以先从左到右扫一遍，左侧楼截断右侧楼，再从右到左扫一遍，右侧楼截断左侧楼。
// 本题很像 积水问题 ，因为最终的目标都是一个外轮廓， 从左向右扫可以决定左斜线，然后从右向左扫可以决定右轮廓线。这里重点是，
// 其中取两个楼之间的最高点的方法是，画几何图形，是一个等腰直角三角形，所以用右斜线的x轴点，减去左斜线的x轴点，除以2，即为等腰直角三角形的高。
class Solution {
    public int maxBuilding(int n, int[][] restrictions) {
        if(restrictions.length == 0)
            return n-1;        
        Arrays.sort(restrictions, (a,b)->Integer.compare(a[0],b[0]));
        restrictions[0][1] = Math.min(restrictions[0][1], restrictions[0][0] - 1);
        for(int i = 0; i < restrictions.length - 1; i++) {
            restrictions[i+1][1] = Math.min(restrictions[i+1][1], restrictions[i][1] + restrictions[i+1][0] - restrictions[i][0]);
        }
        for(int i = restrictions.length-1; i > 0; i--) {
            restrictions[i-1][1] = Math.min(restrictions[i-1][1], restrictions[i][1] + restrictions[i][0] - restrictions[i-1][0]);            
        }
        int height = (restrictions[0][1] + restrictions[0][0] - 1) / 2;
        height = Math.max(height, n - restrictions[restrictions.length - 1][0] + restrictions[restrictions.length - 1][1]);
        for(int i = 0; i < restrictions.length - 1; i++) {
            height = Math.max(height, (-restrictions[i][0] + restrictions[i][1] + restrictions[i+1][0] + restrictions[i+1][1])/2);
        }
        return height;
    }
}
