int calculateLength(struct ListNode* head) {
    int count = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        count += 1;
        temp = temp->next;
    } return count;
}

struct ListNode* middleNodeLogic1(struct ListNode* head) {
    int length = calculateLength(head);
    struct ListNode *temp = head;
    for(int i = 0; i < length / 2; i++) {
        temp = temp->next;
    } return temp;
}

struct ListNode* middleNodeLogic2(struct ListNode* head) {
    struct ListNode *p = head, *q = head;
    while (q && q->next) {
        p = p->next;
        q = q->next->next;
    } return p;
}
