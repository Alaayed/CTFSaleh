# Definition for a binary tree node.
def dfs_depth_sum( root, depth, depth_sum):
        if root == None:
                return 
        depth_sum[depth] += root.val
        dfs_depth_sum(root.left, depth+1, depth_sum)
        dfs_depth_sum(root.right, depth+1, depth_sum)
        return 
def dfs_mod( root, bval, depth, depth_sum):
        if root == None:
                return
        root.val = depth_sum[depth] - bval - root.val
        lval = root.left.val if root.left is not None else 0
        rval = root.right.val if root.right is not None else 0
        dfs_mod(root.left, rval, depth+1,depth_sum)
        dfs_mod(root.right, lval, depth+1,depth_sum)


class TreeNode:
        def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
class Solution:
        def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
                depth_sum = [0 for _ in range(10**5)]
                dfs_depth_sum(root, 0, depth_sum)
                dfs_mod(root, 0, 0, depth_sum)
                return root
