from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root: TreeNode) -> list:
    if not root:
        return None

    res, queue = [], deque([root])

    while queue:
        node = queue.popleft()
        if node and node.val is not None:
            res.append(node.val)
            if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
        else:
            res.append(None)

    return res


def list_to_tree(vals: list) -> TreeNode:
    if not vals:
        return None

    vals = vals[::-1]
    root = TreeNode(vals.pop())
    queue = deque([root])

    while vals and queue:
        node = queue.popleft()

        if node:
            left = vals.pop()
            if left is not None:
                node.left = TreeNode(left)
                queue.append(node.left)

            right = vals.pop()
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)

    return root
