from collections import deque
from os import getenv
from typing import Callable, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root: Optional[TreeNode]) -> list:
    res, queue = [], deque([root] if root else [])

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


def list_to_tree(vals: list[any]) -> Optional[TreeNode]:
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


def use_list_in_test(
    at_input: bool = True,
    at_output: bool = False,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        if getenv("TEST_ENV") != "TRUE":
            return func

        def decorated(*args, **kwargs):
            output = (
                func(
                    # avoid applying the input convertor during recursion
                    *[list_to_tree(arg) if type(arg) is list else arg for arg in args],
                    **kwargs
                )
                if at_input
                else func(*args, **kwargs)
            )
            return tree_to_list(output) if at_output else output

        return decorated

    return decorator
