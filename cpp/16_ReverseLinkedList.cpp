/*
 * Q16. Reverse Linked List (Category: Linked List)
 *
 * Problem: Reverse a singly linked list iteratively.
 *
 * Approach: Maintain prev and curr pointers; re-link each node backward.
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

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;

    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

void printList(ListNode* head) {
    while (head) {
        cout << head->val;
        if (head->next) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // 1 -> 2 -> 3 -> 4 -> 5
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    printList(reverseList(head)); // 5 -> 4 -> 3 -> 2 -> 1
    return 0;
}
