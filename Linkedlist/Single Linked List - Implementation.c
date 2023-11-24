#include<stdio.h>
#include<stdlib.h>

struct Node {
	int data;
	struct Node *next;
};

struct Node *head = NULL;

void printLL(struct Node * head) {
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d->", temp->data);
        temp = temp->next;
    } printf("NULL");
}

struct Node * createNode(int data) {
    struct Node *newNode;
    newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insBeg(int data) {
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        newNode->next = head;
        head = newNode;
    }
}

void insPos(int data, int index) {
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node *temp = head;
        while (index - 1 > 0) {
            temp = temp->next;
            index -= 1;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

void insEnd(int data) {
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node *temp = head;
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = newNode;
    }
}

int main() {
	int i;
	for(i = 0; i < 3; i++) {
	    int data;
	    scanf("%d", &data);
	    insBeg(data);
	}
	for(i = 0; i < 3; i++) {
	    int data;
	    scanf("%d", &data);
	    insEnd(data);
	}
	insPos(20, 2);
	printLL(head);
}
