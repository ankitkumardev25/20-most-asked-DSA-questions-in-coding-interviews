/*
 * Q10. Maximum Depth of Binary Tree (Category: Trees)
 *
 * Problem: Find the maximum depth (height) of a binary tree.
 *
 * Approach: Recursive DFS — depth = 1 + max(left, right).
 *
 * Time Complexity : O(n)
 * Space Complexity: O(h) where h is tree height
 */
#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

int main() {
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15    7
    TreeNode* root = new TreeNode(3);
    root->left  = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left  = new TreeNode(15);
    root->right->right = new TreeNode(7);
    cout << "Max Depth: " << maxDepth(root) << endl; // 3
    return 0;
}
