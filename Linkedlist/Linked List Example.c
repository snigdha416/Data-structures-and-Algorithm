#include<stdio.h>
#include<stdlib.h>

struct Node {
	int data;
	struct Node *next;
};

void printLL(struct Node * head) {
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d->", temp->data);
        temp = temp->next;
    } printf("NULL");
}

int main() {
	struct Node *first, *second, *third, *head;
	
	first = malloc(sizeof(struct Node));
	second = (struct Node *)malloc(sizeof(struct Node));
	third = (struct Node *)malloc(sizeof(struct Node));
	
	first->data = 1;
	first->next = second;
	
	second->data = 2;
	second->next = third;
	
	third->data = 3;
	third->next = NULL;
	
	head = first;
	
// 	printf("%d %d %d\n", first, second, third);
	printf("%d %d %d\n", first->data, second->data, third->data);	
	printLL(head);
}
