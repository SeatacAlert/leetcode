//kuannoodle的解
//思路与我不一样，他先将所有要查询的点query放到TreeMap里，然后用keySet得到TreeSet tset，是一个排了序的query点集合
//所有的interval按长度从小到大排序，然后对于每个区间intv，在tset中找到在这个区间中的点，这些点的最佳长度就更新了，更新以后从tset中移除掉
//这里完美的利用了TreeSet的方法 tset.subSet(start, end) 以及 集合的 tset.add(ele) tset.removeAll(tset2)
//这个方法的缺点是复杂度高，因为对interval和queries都进行了排序。
class Solution {
   public int[] minInterval(int[][] intervals, int[] queries) {

    final Map<Integer, List<Integer>> queryIndices = new HashMap<>();
    for (int i = 0; i != queries.length; i++) {
      final int v = queries[i];
      List<Integer> list = queryIndices.get(v);
      if (list == null)
        queryIndices.put(v, list = new ArrayList<>());
      list.add(i);
    }
    final TreeSet<Integer> tset = new TreeSet<>(queryIndices.keySet());

    int[] res = new int[queries.length];
    Arrays.fill(res, -1);

    Arrays.sort(intervals, (a, b) -> {
      return (a[1] - a[0]) - (b[1] - b[0]);
    });

    for (int[] intv : intervals) {
      final int intvlen = intv[1]+1-intv[0];
      List<Integer> removeem = new ArrayList<>();
      for (Integer queryval : tset.subSet(intv[0], intv[1] + 1)) {
        removeem.add(queryval);
        for (Integer qidx : queryIndices.get(queryval)) {
          res[qidx] = intvlen;
        }
      }
      tset.removeAll(removeem);
    }

    return res;

  }

}
