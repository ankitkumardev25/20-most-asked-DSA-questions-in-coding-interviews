import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Q12. Binary Tree Level Order Traversal (Category: Trees)
 *
 * Problem: Return the level-order (BFS) traversal of a binary tree's node values.
 *
 * Approach: Use a Queue. Process each level by iterating exactly queue.size() times,
 *           then add children for the next level.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
public class LevelOrderTraversal {

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left  != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(level);
        }
        return result;
    }

    public static void main(String[] args) {
        // Tree:  3
        //       / \
        //      9  20
        //        /  \
        //       15    7
        LevelOrderTraversal solution = new LevelOrderTraversal();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        System.out.println(solution.levelOrder(root)); // [[3], [9, 20], [15, 7]]
    }
}
