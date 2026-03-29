"""
Q12. Binary Tree Level Order Traversal (Category: Trees)

Problem: Return the level-order (BFS) traversal of a binary tree.

Approach: BFS with a deque. Process each level by iterating len(queue) times,
          then add children for the next level.

Time Complexity : O(n)
Space Complexity: O(n)
"""
from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if root is None:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)

    return result


if __name__ == "__main__":
    #    3
    #   / \
    #  9  20
    #    /  \
    #   15    7
    root = TreeNode(3, TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(root))  # [[3], [9, 20], [15, 7]]
