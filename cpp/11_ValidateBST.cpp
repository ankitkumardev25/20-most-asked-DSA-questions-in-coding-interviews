/*
 * Q11. Validate Binary Search Tree (Category: Trees)
 *
 * Problem: Determine if a binary tree is a valid BST.
 *
 * Approach: Pass min/max bounds down the recursion. Each node must fall
 *           strictly within (min, max).
 *
 * Time Complexity : O(n)
 * Space Complexity: O(h)
 */
#include <iostream>
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

bool validate(TreeNode* node, long min, long max) {
    if (!node) return true;
    if (node->val <= min || node->val >= max) return false;
    return validate(node->left, min, node->val) &&
           validate(node->right, node->val, max);
}

bool isValidBST(TreeNode* root) {
    return validate(root, (long)INT_MIN - 1, (long)INT_MAX + 1);
}

int main() {
    cout << boolalpha;

    // Valid BST: 2 / 1 / 3
    TreeNode* r1 = new TreeNode(2);
    r1->left  = new TreeNode(1);
    r1->right = new TreeNode(3);
    cout << isValidBST(r1) << endl; // true

    // Invalid BST: 5 / 1 / 4(3,6)
    TreeNode* r2 = new TreeNode(5);
    r2->left  = new TreeNode(1);
    r2->right = new TreeNode(4);
    r2->right->left  = new TreeNode(3);
    r2->right->right = new TreeNode(6);
    cout << isValidBST(r2) << endl; // false
    return 0;
}
