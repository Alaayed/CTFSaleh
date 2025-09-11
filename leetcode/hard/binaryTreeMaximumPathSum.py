from typing import Optional, Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)[0]
    def rec(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if (root == None):
            return (-1e9,-1e9)
        left = self.rec(root.left)
        right = self.rec(root.right)
        # best path in tree or subtrees, best path terminating here
        include_both = left[1] + right[1] + root.val
        include_root = max(left[1], right[1], 0) + root.val
        best = max(left[0], right[0], include_both, include_root)
        return best, include_root