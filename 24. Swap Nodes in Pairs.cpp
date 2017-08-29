/*
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
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
    ListNode* swapPairs(ListNode* head) {
        ListNode* a, *b;
        ListNode* go = head;
        int x = 0;
        while (go != NULL) {
            x++;
            if (x % 2 == 1) {
                a = go;
            } else {
                b = go;
                int tmp = a->val;                
                a->val = b->val;
                b->val = tmp;
            }
            go = go->next;
        }
        
        return head;
    }
};