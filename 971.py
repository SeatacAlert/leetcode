class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        def flip(root, voyage, i, res):
            if i > len(voyage):
                return -1
            if (not root.left and not root.right):
                if len(voyage) > i and voyage[i] == root.val:
                    return i+1
                else:
                    return -1
            elif not root.left or not root.right:
                if len(voyage) < i+2 or root.val != voyage[i]:
                    return -1
                else:
                    node = root.right if not root.left else root.left
                    return flip(node, voyage, i+1, res)
            else:
                if len(voyage) < i+3 or root.val != voyage[i]:
                    return -1
                else:
                    if voyage[i+1] != root.left.val:
                        root.left, root.right = root.right, root.left
                        res.append(root.val)
                    if voyage[i+1] != root.left.val:
                        return -1
                    else:
                        left_end = flip(root.left, voyage, i+1, res)
                        if left_end == -1:
                            return -1
                        else:
                            right_end = flip(root.right, voyage, left_end, res)
                            return right_end
        if flip(root, voyage, 0, res) == len(voyage):
            return res
        else:
            return [-1]
