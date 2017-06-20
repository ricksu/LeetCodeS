/*
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* head1 = new ListNode(0);
        ListNode* head2 = new ListNode(0);
        
        ListNode* h1 = head1;
        ListNode* h2 = head2;
        while (head != NULL) {
            if (head->val < x) {
                h1->next = head;
                head = head->next;
                h1 = h1->next;
            } else {
                h2->next = head;
                head = head->next;
                h2 = h2->next;
            }
        }
            h1->next = head2->next;
            h2->next = NULL;
            ListNode* result = head1->next;
            free(head1);
            free(head2);
            
            return result;
        }
    
};