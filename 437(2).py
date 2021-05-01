class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.result = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        self.dfs(root, targetSum, 0, sum_count)
        return self.result
    def dfs(self, root, targetSum, currPathSum, sum_count):
        if root is None:
            return
        currPathSum += root.val
        self.result += sum_count[currPathSum - targetSum]
        sum_count[currPathSum] = sum_count[currPathSum] + 1
        self.dfs(root.left, targetSum, currPathSum, sum_count)
        self.dfs(root.right, targetSum, currPathSum, sum_count)        
        sum_count[currPathSum] -= 1
        
