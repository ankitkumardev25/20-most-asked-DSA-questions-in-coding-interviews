"""
Q13. Lowest Common Ancestor of a Binary Tree (Category: Trees)

Problem: Find the lowest common ancestor (LCA) of two nodes p and q.

Approach: Recursive post-order. Return the node if it matches p or q.
          If both subtrees return non-None, current node is LCA.

Time Complexity : O(n)
Space Complexity: O(h)
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


def lowest_common_ancestor(root: Optional[TreeNode],
                            p: TreeNode,
                            q: TreeNode) -> Optional[TreeNode]:
    if root is None or root is p or root is q:
        return root
    left  = lowest_common_ancestor(root.left,  p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root  # p and q in different subtrees
    return left or right


if __name__ == "__main__":
    #         3
    #        / \
    #       5   1
    #      / \
    #     6   2
    #          \
    #           4
    n6, n4 = TreeNode(6), TreeNode(4)
    n2 = TreeNode(2, right=n4)
    n5 = TreeNode(5, n6, n2)
    n1 = TreeNode(1)
    root = TreeNode(3, n5, n1)

    lca = lowest_common_ancestor(root, n5, n4)
    print(lca.val)  # 5

    lca2 = lowest_common_ancestor(root, n5, n1)
    print(lca2.val)  # 3
