/**
 * Q11. Validate Binary Search Tree (Category: Trees)
 *
 * Problem: Determine if a binary tree is a valid BST.
 *          A valid BST has: left subtree values < node value < right subtree values.
 *
 * Approach: Pass a min/max range down the recursion. Each node must fall
 *           strictly within (min, max).
 *
 * Time Complexity : O(n)
 * Space Complexity: O(h) where h is tree height
 */
public class ValidateBST {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean validate(TreeNode node, long min, long max) {
        if (node == null) return true;
        if (node.val <= min || node.val >= max) return false;
        return validate(node.left, min, node.val) &&
               validate(node.right, node.val, max);
    }

    public static void main(String[] args) {
        ValidateBST solution = new ValidateBST();

        // Valid BST:  2
        //            / \
        //           1   3
        TreeNode root1 = new TreeNode(2);
        root1.left = new TreeNode(1);
        root1.right = new TreeNode(3);
        System.out.println(solution.isValidBST(root1)); // true

        // Invalid BST: 5
        //             / \
        //            1   4
        //               / \
        //              3   6
        TreeNode root2 = new TreeNode(5);
        root2.left = new TreeNode(1);
        root2.right = new TreeNode(4);
        root2.right.left = new TreeNode(3);
        root2.right.right = new TreeNode(6);
        System.out.println(solution.isValidBST(root2)); // false
    }
}
