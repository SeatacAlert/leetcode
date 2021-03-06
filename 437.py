# 假设已经保存i-j的和，那么需要添加第j+1个元素的时候，每个元素都要加j+1，麻烦
# 所以假定所有的元素都减去了1--j+1
# 因此实际上这里保存的是-(1--i)的和
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        cnt = {}
        return self.dfs(0, cnt, root, targetSum)
    
    def dfs(self, base, val, root, targetSum):
        if not root:
            return 0
        res = 0
        base += root.val
        new_val = root.val - base
        if new_val not in val:
            val[new_val] = 1
        else:
            val[new_val] += 1
        if targetSum - base in val:
            res += val[targetSum - base]
        res += self.dfs(base, val, root.left, targetSum)
        res += self.dfs(base, val, root.right, targetSum)
        val[new_val] -= 1
        return res
