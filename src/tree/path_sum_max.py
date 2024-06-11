#
# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
from .tree_node import TreeNode, use_list_in_test


@use_list_in_test()
def maxPathSum(root: TreeNode) -> int:
    """A path can be expanded from any node.

    1) DFS & Backtracking
    search down at every node as the root of the path
    as well as returning the max connecting value to its parent

    time complexity: O(N), space complexity: O(N)
    * N is the number of nodes
    """
    res = -float("inf")

    def search(node: TreeNode) -> int:
        nonlocal res

        if not node:
            return 0

        left_max = max(search(node.left), 0)
        right_max = max(search(node.right), 0)

        res = max(res, node.val + left_max + right_max)
        return node.val + max(left_max, right_max)

    search(root)

    return res
