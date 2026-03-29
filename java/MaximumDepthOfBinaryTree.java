/**
 * Q10. Maximum Depth of Binary Tree (Category: Trees)
 *
 * Problem: Find the maximum depth (height) of a binary tree.
 *
 * Approach: Recursion — depth = 1 + max(left depth, right depth).
 *
 * Time Complexity : O(n)
 * Space Complexity: O(h) where h is tree height (recursion stack)
 */
public class MaximumDepthOfBinaryTree {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    public static void main(String[] args) {
        // Tree:   3
        //        / \
        //       9  20
        //         /  \
        //        15    7
        MaximumDepthOfBinaryTree solution = new MaximumDepthOfBinaryTree();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        System.out.println("Max Depth: " + solution.maxDepth(root)); // 3
    }
}
