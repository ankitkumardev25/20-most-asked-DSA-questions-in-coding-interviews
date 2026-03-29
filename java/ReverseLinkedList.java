/**
 * Q16. Reverse Linked List (Category: Linked List)
 *
 * Problem: Reverse a singly linked list iteratively.
 *
 * Approach: Maintain three pointers: prev, curr, and next.
 *           Re-link each node to point backward, then advance all pointers.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class ReverseLinkedList {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    private static void printList(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null) {
            sb.append(head.val);
            if (head.next != null) sb.append(" -> ");
            head = head.next;
        }
        System.out.println(sb);
    }

    public static void main(String[] args) {
        // 1 -> 2 -> 3 -> 4 -> 5
        ReverseLinkedList solution = new ReverseLinkedList();
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        printList(solution.reverseList(head)); // 5 -> 4 -> 3 -> 2 -> 1
    }
}
