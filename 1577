from collections import Counter
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = Counter([i*i for i in nums1])
        n2 = Counter([i*i for i in nums2])
        n11 = sum([n2[item1*item2] for i,item1 in enumerate(nums1) for j,item2 in enumerate(nums1) if i < j])
        n22 = sum([n1[item1*item2] for i,item1 in enumerate(nums2) for j,item2 in enumerate(nums2) if i < j])
        return n11 + n22
        
"""
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # lengths [1, 10**3], elements [1, 10**5]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        for n in nums1:
            cnt1[n] += 1
        for n in nums2:
            cnt2[n] += 1

        def triplets(arr1, arr2):
            ans = 0
            for t, v in arr1.items():
                k = arr2.get(t, 0)
                tmp = k * (k - 1) // 2
                sq = t * t
                for m in arr2:
                    if m < t and sq % m == 0:
                        tmp += arr2.get(m, 0) * arr2.get(sq // m, 0)
                ans += tmp * v
            return ans
        return triplets(cnt1, cnt2) + triplets(cnt2, cnt1)
        
        """
