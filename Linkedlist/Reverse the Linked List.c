struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *current = head, *prev = NULL, *forward = NULL;
    while (current) {
        forward = current->next;
        current->next = prev;
        prev = current;
        current = forward;
    }  return prev;
}
