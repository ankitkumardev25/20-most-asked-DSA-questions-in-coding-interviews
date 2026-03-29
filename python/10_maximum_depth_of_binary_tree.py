"""
Q10. Maximum Depth of Binary Tree (Category: Trees)

Problem: Find the maximum depth (height) of a binary tree.

Approach: Recursive DFS — depth = 1 + max(left depth, right depth).

Time Complexity : O(n)
Space Complexity: O(h) where h is tree height
"""
from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15    7
    root = TreeNode(3, TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root))  # 3
