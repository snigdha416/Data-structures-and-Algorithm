bool hasCycle(struct ListNode *head) {
    struct ListNode *p = head, *q = head;
    while (q && q->next) {
        p = p->next;
        q = q->next->next;
        if (p == q) return true;
    } return false;
}
