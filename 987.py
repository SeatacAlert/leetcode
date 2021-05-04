# 我的慢解
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        cols = {}
        records = {}
        def dfs(root, r, c):
            if not root: return
            if (c,r) not in records:
                records[(c,r)] = list()
            cols[c] = max(cols.get(c,0), r)
            records[(c,r)].append(root.val)
            dfs(root.left, r+1, c-1)
            dfs(root.right, r+1, c+1)
        dfs(root, 0, 0)
        col_keys = cols.keys()
        min_col = min(col_keys)
        max_col = max(col_keys)
        res = []
        for col in range(min_col, max_col+1):
            col_res = []
            for row in range(0, cols[col]+1):
                if (col, row) in records:
                    col_res.extend(sorted(records[(col, row)]))
            res.append(col_res)
        return res

# 最快的解
# 用到了deque，双端队列，而且没用dfs，用的是bfs，因为dfs会先到底部，但是bfs是按层执行，更符合此题最终目标
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [[root.val]]
        
        queue = collections.deque()
        queue.append((root, 0))
        
        vertical_map = collections.defaultdict(list)
        
        while queue:
            new_queue = collections.deque()
            vertical = collections.defaultdict(list)
            for node, vert in queue:
                vertical[vert].append(node.val)
                if node.left:
                    new_queue += (node.left, vert - 1),
                if node.right:
                    new_queue += (node.right, vert + 1),
            for vert in vertical:
                vertical_map[vert].extend(sorted(vertical[vert]))
            queue = new_queue
            
        return [vertical_map[vert] for vert in sorted(vertical_map)]
