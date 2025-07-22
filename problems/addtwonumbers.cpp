/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        int carry = 0;

        while (l1 || l2 || carry) {
            int val1 = l1 ? l1->val: 0; // if l1 is true, get the val of the node that l1 point to
            int val2 = l2 ? l1->val: 0;
            int sum = val1 + val2 + carry;

            carry = sum / 10;
            curr->next = new ListNode(sum % 10);
            curr = curr->next; // move on to the next node
            
            if (l1) l1 = l1->next; // if l1 is true, move on to the next node
            if (l2) l2 = l2->next;
            }
            
            return dummy->next;
        }
};
