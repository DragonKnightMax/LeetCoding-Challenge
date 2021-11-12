/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // Add dummy head before real head
        ListNode b4Head = new ListNode(-1);
        b4Head.next = head;
        ListNode curr = b4Head;
        
        // Use one pointer instead of 2 to represent prev and curr
        while (curr.next != null) {
            if (curr.next.val == val) {
                curr.next = curr.next.next;
            }
            else {
                curr = curr.next;
            }
        }
        
        return b4Head.next;
    }
}
