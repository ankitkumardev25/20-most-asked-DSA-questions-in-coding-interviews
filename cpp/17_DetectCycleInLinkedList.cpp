/*
 * Q17. Detect Cycle in Linked List (Category: Linked List)
 *
 * Problem: Detect if a linked list has a cycle.
 *
 * Approach: Floyd's slow-fast pointer algorithm.
 *           If they meet, a cycle exists.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    cout << boolalpha;

    // Cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
    ListNode* head = new ListNode(3);
    ListNode* n2   = new ListNode(2);
    ListNode* n0   = new ListNode(0);
    ListNode* n4   = new ListNode(-4);
    head->next = n2; n2->next = n0; n0->next = n4;
    n4->next = n2; // cycle
    cout << "Has cycle: " << hasCycle(head) << endl; // true

    // No cycle: 1 -> 2
    ListNode* nc = new ListNode(1);
    nc->next = new ListNode(2);
    cout << "Has cycle: " << hasCycle(nc) << endl; // false
    return 0;
}
