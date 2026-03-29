"""
10. Invert Binary Tree
Given the root of a binary tree, invert the tree (mirror it), and return its root.

Example:
         4                   4
       /   \               /   \
      2     7    -->      7     2
     / \   / \           / \   / \
    1   3 6   9         9   6 3   1

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def level_order(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(root)
    print(level_order(inverted))  # [4, 7, 2, 9, 6, 3, 1]
