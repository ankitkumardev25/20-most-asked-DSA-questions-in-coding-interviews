/**
 * Q13. Lowest Common Ancestor of a Binary Tree (Category: Trees)
 *
 * Problem: Find the lowest common ancestor (LCA) of two given nodes p and q.
 *
 * Approach: Recursive post-order search. If the current node matches p or q,
 *           return it. If both left and right subtrees return non-null, current
 *           node is the LCA.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(h) where h is tree height
 */
public class LowestCommonAncestor {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;

        TreeNode left  = lowestCommonAncestor(root.left,  p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        // p and q found in different subtrees — current node is LCA
        if (left != null && right != null) return root;
        return (left != null) ? left : right;
    }

    public static void main(String[] args) {
        //         3
        //        / \
        //       5   1
        //      / \ / \
        //     6  2 0  8
        //       / \
        //      7   4
        LowestCommonAncestor solution = new LowestCommonAncestor();
        TreeNode root = new TreeNode(3);
        TreeNode n5   = new TreeNode(5);
        TreeNode n1   = new TreeNode(1);
        TreeNode n6   = new TreeNode(6);
        TreeNode n2   = new TreeNode(2);
        TreeNode n4   = new TreeNode(4);
        root.left  = n5;  root.right = n1;
        n5.left    = n6;  n5.right   = n2;
        n2.right   = n4;
        n1.left    = new TreeNode(0); n1.right = new TreeNode(8);

        System.out.println("LCA(5,4): " + solution.lowestCommonAncestor(root, n5, n4).val); // 5
        System.out.println("LCA(5,1): " + solution.lowestCommonAncestor(root, n5, n1).val); // 3
    }
}
