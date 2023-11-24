int calculateLength(struct ListNode* head) {
    int count = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        count += 1;
        temp = temp->next;
    } return count;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    int length1 = calculateLength(headA);
    int length2 = calculateLength(headB);
    if (length1 > length2) {
        int diff = length1 - length2;
        while (diff--) headA = headA->next;
    } else {
        int diff = length2 - length1;
        while (diff--) headB = headB->next;
    }
    while (headA && headB) {
        if(headA == headB) return headA;
        headA = headA->next;
        headB = headB->next;
    } return NULL;
}
