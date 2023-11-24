#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
	int data;
	struct Node *next;
} node;

node *head = NULL;

node * createNode(int data) {
	node *newNode = (node *)malloc(sizeof(node));
	newNode->data = data;
	newNode->next = NULL;
	return newNode;
}

node * insBeg(int data) {
	node *newNode = createNode(data);
	if (head == NULL) {
		head = newNode;
	} else {
		newNode->next = head;
		head = newNode;
	} return head;
}

node * insPos(int data, int index) {
	node *newNode = createNode(data);
	if (head == NULL) {
		head = newNode;
	} else {
		if (index == 0) {
			return insBeg(data);
		}
		node *temp = head;
		while (index - 1) {
			temp = temp->next;
			index -= 1;
		}
		newNode->next = temp->next;
		temp->next = newNode;
	}	return head;
}

node * insEnd(int data) {
	node *newNode = createNode(data);
	if (head == NULL) {
		head = newNode;
	} else {
		node *temp = head;
		while (temp->next) temp = temp->next;
		temp->next = newNode;
	} return head;
}

node * delBeg() {
	if(head == NULL) return head;
	return head->next;
}

node * delPos(int index) {
	if(head == NULL) return head;
	if (index == 0) return delBeg();
	node *temp = head;
	while (index - 1 > 0) {
		printf("Del Pos\n");
		temp = temp->next;
		index -= 1;
	}
	temp->next = temp->next->next;
	return head;
}

node * delEnd() {
	if(head == NULL) return head;
	node *temp = head;
	while (temp->next->next) temp = temp->next;
	temp->next = NULL;
	return head;
}

void printLL(node *head) {
	node *temp = head;
	while (temp) {
		printf("%d -> ", temp->data);
		temp = temp->next;
		
	}	printf("NULL");
}

int calculateLength(node * head) {
	int count = 0;
	node *temp = head;
	while (temp) {
		count += 1;
		temp = temp->next;
	} return count;
}

int main() {	
 	// 0 - 1 - 3 - 4 - 5 - 9 - 13 - 15 - Null
	head = insBeg(5);
	head = insBeg(3);
	head = insBeg(1);
	head = insEnd(9);
	head = insEnd(13);
	head = insPos(4, 2);
	head = insPos(15, 6);
	head = insPos(0, 0);
//	head = delBeg();
//	head = delBeg();
//	head = delEnd();
//	head = delEnd();
//	head = delPos(0);
	printLL(head);
	int length = calculateLength(head);
	printf("\n%d", length);
}
