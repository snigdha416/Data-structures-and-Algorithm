#include<stdio.h>

struct Node {
	int data;
	struct Node *next;
};

struct Node *head;

int main() {
	struct Node *first, *second, *third;
	first->data = 1;
	first->next = NULL;
	
	second->data = 2;
	second->next = NULL;
	
	third->data = 3;
	third->next = NULL;
	
	printf("%d %d %d\n", first, second, third);
	printf("%d %d %d\n", first->data, second->data, third->data);	
	
}
