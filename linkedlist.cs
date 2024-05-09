public class Solution {
    public bool HasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next; 
        if (head == null || head.next == null) {
            return false;
        }
        while (fast != null && fast.next != null) {
            if (slow == fast) {
                return true; 
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return false;
    }
}
