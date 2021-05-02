//这是uwi的方法
//因为题目已知s的长度不超过20
//所以用long可以解决
//Long.parseLong/parseUnsignedLong(s, [radix]) 这个函数的返回值是 long 类型
//Long.valueOf(long/string) 的返回值是 Long 类型
//Long.toString/toUnsignedString/toBinaryString/toOctalString/toHexString 是转字符串的方法
class Solution {
		public boolean splitString(String s) {
			int n = s.length();
			for(int i = 1;i < n;i++) {
				if (dfs(s, i, Long.parseUnsignedLong(s.substring(0, i)))) return true;
			}
			return false;
		}

		boolean dfs(String s, int pos, long preu)
		{
			long tar = preu - 1;
			int n = s.length();
			if(pos == n)return true;
			for(int i = pos+1;i <= n;i++){
				long f = Long.parseUnsignedLong(s.substring(pos, i));
				if(tar == f && dfs(s, i, f)){
					return true;
				}
			}
			return false;
		}
	}

//如果你不能记住这个函数，那么也可以一位一位往上加
class Solution {
  public boolean splitString(String s) {
    boolean res = false;
    long number = 0;
    for (int i = 0; i + 1 != s.length(); i++) {
      number = number * 10L + (s.charAt(i) - '0');
      if (dfs(s, i + 1, number)) {
        res = true;
        break;
      }
    }
    return res;
  }

  private boolean dfs(String s, int pos, final long set) {
    if (pos >= s.length())
      return true;
    long number = 0;
    boolean res = false;
    for (int i = pos; i != s.length(); i++) {
      number = number * 10 + s.charAt(i) - '0';
      if (number + 1L == set) {
        if (dfs(s, i + 1, number)) {
          res = true;
          break;
        }
      }
      if (number - 1L > set)
        break;
    }
    return res;
  }
}

//当然也可以使用大整数
import java.math.BigInteger;

class Solution {
    boolean splitString(String s, int index, BigInteger last) {
        if (index == s.length()) {
            return true;
        }
        BigInteger data = BigInteger.ZERO;
        for (int i = index;i < s.length();i++) {
            data = data.multiply(BigInteger.valueOf(10)).add(BigInteger.valueOf(s.charAt(i) - '0'));
            if (last.equals(data.add(BigInteger.ONE)) && splitString(s, i + 1, data)) {
                return true;
            }
        }
        return false;
    }
    public boolean splitString(String s) {
        BigInteger data = BigInteger.ZERO;
        for (int i = 0;i + 1 < s.length();i++) {
            data = data.multiply(BigInteger.valueOf(10)).add(BigInteger.valueOf(s.charAt(i) - '0'));
            if (splitString(s, i + 1, data)) {
                return true;
            }
        }
        return false;
    }
}
