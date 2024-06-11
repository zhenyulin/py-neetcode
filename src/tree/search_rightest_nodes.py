#
# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
#
from collections import deque

from .tree_node import TreeNode, use_list_in_test


@use_list_in_test()
def rightSideView(root: TreeNode) -> list[int]:
    """To have all the rightest nodes.

    we can search level by level

    1) BFS

    time complexity: O(N), space complexity: O(N)
    * N is the number of Nodes
    """
    queue, res = deque([root] if root else []), []

    while queue:
        res.append(queue[-1].val)

        for _ in range(len(queue)):
            node = queue.pop()
            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)

    return res
