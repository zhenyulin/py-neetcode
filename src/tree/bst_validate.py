#
# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
#
from typing import Optional
from .tree_node import TreeNode, use_list_in_test


@use_list_in_test()
def validateBST(root: Optional[TreeNode]) -> bool:
    """
    for BST, we need to cascade down the node.val
    as the min(low) on the right and max(high) on the left

    1) Recursion

    time complexity: O(N), space complexity: O(N)
    * N is the number of Nodes
    """

    def check(node, low, high):
        return not node or (
            low < node.val < high
            and check(node.left, low, node.val)
            and check(node.right, node.val, high)
        )

    return check(root, -float("inf"), float("inf"))
