"""
Q11. Validate Binary Search Tree (Category: Trees)

Problem: Determine if a binary tree is a valid BST.

Approach: Pass min/max bounds down the recursion. Each node must fall
          strictly within (min, max).

Time Complexity : O(n)
Space Complexity: O(h)
"""
from __future__ import annotations
from typing import Optional
import math


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and \
               validate(node.right, node.val, high)

    return validate(root, -math.inf, math.inf)


if __name__ == "__main__":
    # Valid BST
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(root1))  # True

    # Invalid BST
    root2 = TreeNode(5, TreeNode(1),
                     TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(root2))  # False
