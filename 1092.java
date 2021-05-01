// 普通dp题
// 但是有一个想回找的过程，为了想回找路径，我设置了choose作为标记。
// 别人的代码比我好的地方在于，第一不需要标记，只要比较字符和dp的值就知道当时是选的哪个。
// 第二，先将String转换为toCharArray能够节约时间。最后就是sb.reverse().toString()
class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int[][] dp = new int[str1.length()+1][str2.length()+1];
        int[][] choose = new int[str1.length()+1][str2.length()+1];
        for(int i = 0; i < str1.length() + 1; i++) {
            dp[i][0] = i;
            choose[i][0] = 1;
        }            
        for(int i = 0; i < str2.length() + 1; i++) {
            dp[0][i] = i;
            choose[0][i] = 2;
        }
            
        for(int i = 1; i < str1.length() + 1; i++)
            for(int j = 1; j < str2.length() + 1; j++)
            {
                if (str1.charAt(i-1) == str2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    choose[i][j] = 3;
                }
                else {
                    if (dp[i-1][j] < dp[i][j-1]) {
                        dp[i][j] = dp[i-1][j] + 1;
                        choose[i][j] = 1;
                    } else {
                        dp[i][j] = dp[i][j-1] + 1;
                        choose[i][j] = 2;
                    }
                }
            }
        StringBuilder sb = new StringBuilder();
        int i = str1.length();
        int j = str2.length();
        while(i != 0 || j != 0) {
            if (choose[i][j] == 3) {
                sb.append(str1.charAt(i-1));
                i--; j--;
            }
            else if (choose[i][j] == 2) {
                sb.append(str2.charAt(j-1));
                j--;
            } else if (choose[i][j] == 1) {
                sb.append(str1.charAt(i-1));
                i--;
            }
        }
        return sb.reverse().toString();
    }
}
