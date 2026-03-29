/*
 * Q13. Lowest Common Ancestor of a Binary Tree (Category: Trees)
 *
 * Problem: Find the lowest common ancestor (LCA) of two nodes p and q.
 *
 * Approach: Recursive post-order. Return the node if it matches p or q.
 *           If both left and right return non-null, current node is LCA.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(h)
 */
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;

    TreeNode* left  = lowestCommonAncestor(root->left,  p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);

    if (left && right) return root;   // p and q in different subtrees
    return left ? left : right;
}

int main() {
    //         3
    //        / \
    //       5   1
    //      / \
    //     6   2
    //          \
    //           4
    TreeNode* root = new TreeNode(3);
    TreeNode* n5   = new TreeNode(5);
    TreeNode* n1   = new TreeNode(1);
    TreeNode* n6   = new TreeNode(6);
    TreeNode* n2   = new TreeNode(2);
    TreeNode* n4   = new TreeNode(4);
    root->left  = n5;  root->right = n1;
    n5->left    = n6;  n5->right   = n2;
    n2->right   = n4;

    cout << "LCA(5,4): " << lowestCommonAncestor(root, n5, n4)->val << endl; // 5
    cout << "LCA(5,1): " << lowestCommonAncestor(root, n5, n1)->val << endl; // 3
    return 0;
}
