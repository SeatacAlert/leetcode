//我的解: 
//unionfind，所谓unionfind其实就是给每个元素一个祖先，方便判断它们是否在同一支中
//有两个指标：是否有环；是否有双parnt
//如果有环，那么目标必在环上，为发现环的那条边
//如果有双parent，那么目标必为双parent中的一个
//如果都有，那么目标为双parent的在环上的那条边
class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int n = edges.length;
        int[] ancester = new int[n+1];
        int target = 0;
        int circle = 0;
        int parent = 0;
        for(int i = 0; i < n; i++) {
            int a = edges[i][0];
            while(ancester[a] != 0) {
                a = ancester[a];
            }
            int b = edges[i][0];
            while(b != a) {
                int c = ancester[b];
                ancester[b] = a;
                b = c;
            }
            if (ancester[edges[i][1]] != 0) {
                target = edges[i][1];
                parent = edges[i][0];
            }
            if(a == edges[i][1]) 
                circle = edges[i][0];
            else if (ancester[edges[i][1]] == 0) {
                ancester[edges[i][1]] = a;
            }
            //System.out.printf("%d %d %d\n", target, parent, circle);
        }
        if (target == 0) {
            return new int[]{circle, ancester[circle]};
        } else {
            if (circle == 0) {
                return new int[]{parent, target};
            } else {
                for(int i = 0; i < n; i++) {
                    if(edges[i][1] == target && edges[i][0] != parent)
                        return edges[i];
                }
                return null;
            }
        }
    }
}

