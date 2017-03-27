
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* rt = new ListNode(0);
        ListNode* head = rt;
        int upbit = 0;
        ListNode* current = head;
        while(l1 != NULL || l2 != NULL) {
            ListNode* tmp = new ListNode(0);
            if (upbit == 1) {
                tmp->val++;
                upbit = 0;
            }
            if (l1 != NULL) {
                tmp->val += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                tmp->val += l2->val;
                l2 = l2->next;
            }
            int sum = tmp->val;
            upbit = sum / 10;
            tmp->val = sum % 10; 
            current->next = tmp;
            current = tmp;
        }
        
        if (l1 == NULL && l2 == NULL && upbit == 1) {
            //last bit
            ListNode* tmp = new ListNode(1);
            current->next = tmp;
        }
        rt = rt->next;
        delete head;
        return rt;
    }
};

//Better solution

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode preHead(0), *p = &preHead;
    int extra = 0;
    while (l1 || l2 || extra) {
        int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + extra;
        extra = sum / 10;
        p->next = new ListNode(sum % 10);
        p = p->next;
        l1 = l1 ? l1->next : l1;
        l2 = l2 ? l2->next : l2;
    }
    return preHead.next;
}