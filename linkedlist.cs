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
public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int pMerge = m + n - 1;
                while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[pMerge] = nums1[p1];
                p1--;
            } else {
                nums1[pMerge] = nums2[p2];
                p2--;
            }
            pMerge--;
        }
        while (p2 >= 0) {
            nums1[pMerge] = nums2[p2];
            p2--;
            pMerge--;
        }
    }
}
