# 二叉树必须用dfs，但是dfs也可以通过保存状态的方式来节约量 
# 最佳解
from functools import lru_cache

class Solution:    
    def generateTrees(self, n: int) -> List[TreeNode]:
        @lru_cache(None)
        def solve(s, e):
            if s > e:
                return (None,)
            
            if s == e:
                return (TreeNode(s),)
            
            return tuple(TreeNode(k, l, r)
                         for k in range(s, e+1)
                         for l in solve(s, k-1)
                         for r in solve(k+1, e))
        
        return solve(1, n)

# 我的解，里面包含了一个deepcopy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def deepcopy(node):
            return node
#            if not node:return None
#            n  = TreeNode(node.val, deepcopy(node.left), deepcopy(node.right))
#            return n
        
        def dfs(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            res = []
            for i in range(start, end+1):
                leftNodes = [None]
                rightNodes = [None]
                if (i > start):
                    leftNodes = dfs(start, i-1)
                if (i < end):
                    rightNodes = dfs(i+1, end)
                for leftnode in leftNodes:
                    for rightnode in rightNodes:
                        node = TreeNode(i, deepcopy(leftnode), deepcopy(rightnode))
                        res.append(node)
            return res
        
        return dfs(1, n)
