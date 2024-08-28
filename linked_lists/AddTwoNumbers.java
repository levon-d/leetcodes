/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     long val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(long val) { this.val = val; }
 *     ListNode(long val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean carry = false; 
        ListNode dummy = new ListNode(0); dummy.next = new ListNode();
        ListNode currentNode = dummy.next; 

        while (l1!=null || l2!=null) { 
            int num1 = l1 == null ? 0 : l1.val;
            int num2 = l2 == null ? 0 : l2.val;
            int val = num1+num2; 

            val = carry ? ++val : val;
            carry = val >= 10 ? true : false; 
            val = val >= 10 ? val % 10 : val;

            currentNode.val = val;
            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;

            if (l1 != null || l2 != null) {
                currentNode.next = new ListNode(); 
                currentNode = currentNode.next;
            } else {
                if (carry) {
                    currentNode.next = new ListNode(1);
                }
            }
        }
        return dummy.next;
    }
}
