/*
 * Q12. Binary Tree Level Order Traversal (Category: Trees)
 *
 * Problem: Return the level-order (BFS) traversal of a binary tree.
 *
 * Approach: BFS with a queue. Process each level by iterating queue.size() times.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> level;
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left)  q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(level);
    }
    return result;
}

int main() {
    //    3
    //   / \
    //  9  20
    //    /  \
    //   15    7
    TreeNode* root = new TreeNode(3);
    root->left  = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left  = new TreeNode(15);
    root->right->right = new TreeNode(7);

    auto res = levelOrder(root);
    for (auto& level : res) {
        cout << "[";
        for (int i = 0; i < (int)level.size(); i++) {
            cout << level[i];
            if (i + 1 < (int)level.size()) cout << ", ";
        }
        cout << "] ";
    }
    cout << endl; // [3] [9, 20] [15, 7]
    return 0;
}
