int calculateLength(struct ListNode* head) {
    int count = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        count += 1;
        temp = temp->next;
    } return count;
}

struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL) return head;
    struct ListNode *p = head, *q = head;
    int size = calculateLength(head); 
    k = k % size;
    while (k > 0) {
        q = q->next;
        k -= 1;
    }
    while (q->next) {
        p = p->next;
        q = q->next;
    }
    q->next = head;
    head = p->next;
    p->next = NULL;
    return head;
}
