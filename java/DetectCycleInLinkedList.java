/**
 * Q17. Detect Cycle in Linked List (Category: Linked List)
 *
 * Problem: Determine if a linked list has a cycle.
 *
 * Approach: Floyd's slow-fast pointer algorithm.
 *           If they ever meet, there is a cycle.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class DetectCycleInLinkedList {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        DetectCycleInLinkedList solution = new DetectCycleInLinkedList();

        // Create cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
        ListNode head = new ListNode(3);
        ListNode n2   = new ListNode(2);
        ListNode n0   = new ListNode(0);
        ListNode n4   = new ListNode(-4);
        head.next = n2;  n2.next = n0;  n0.next = n4;
        n4.next = n2; // cycle

        System.out.println("Has cycle: " + solution.hasCycle(head)); // true

        // No cycle: 1 -> 2
        ListNode nc = new ListNode(1);
        nc.next = new ListNode(2);
        System.out.println("Has cycle: " + solution.hasCycle(nc));  // false
    }
}
