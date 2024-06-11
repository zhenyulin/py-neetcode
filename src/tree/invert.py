#
# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
#
from typing import Optional

from .tree_node import TreeNode, use_list_in_test


@use_list_in_test(at_output=True)
def invert(node: Optional[TreeNode]) -> Optional[TreeNode]:
    """Switch the left and right of every node.

    1) Recursion

    time complexity: O(N), space complexity: O(N)
    """
    if not node:
        return None

    node.left, node.right = node.right, node.left
    invert(node.left)
    invert(node.right)
    return node
