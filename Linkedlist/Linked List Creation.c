#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
	int data;
	struct Node *next;
} node;

int main() {	
	node *head, *first, *second, *third, *temp;
	
	// allocate memory
	first = (struct Node *)malloc(sizeof(struct Node));
	second = (struct Node *)malloc(sizeof(struct Node));
	third = (struct Node *)malloc(sizeof(struct Node));
	
	// Assign the data
	first->data = 1;
	first->next = NULL;
	
	second->data = 2;
	second->next = NULL;
	
	third->data = 3;
	third->next = NULL;
	
	first->next = second;
	second->next = third;
	
	head = first;
	
	// Printing the linked list
	temp = head;
	while (temp) {
		printf("%d -> ", temp->data);
		temp = temp->next;
	}	printf("NULL");
	
	
	// 0, false, 0.00, 0 + 0j, "", [], (), {}, None, NULL
	// 1, 0.45, 1.7, true, 2 + 3j, 'a', "Hello", [1, 2, 3]
	
	
	
}
