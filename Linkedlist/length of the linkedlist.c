int calculateLength(struct ListNode* head) {
    int count = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        count += 1;
        temp = temp->next;
    } return count;
}
