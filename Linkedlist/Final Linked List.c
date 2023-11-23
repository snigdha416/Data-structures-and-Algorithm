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

struct Node * insBeg(int data) {
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        newNode->next = head;
        head = newNode;
    }
    return head;
}

struct Node * insPos(int data, int index) {
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node *temp = head;
        if (index == 0) {
            head = insBeg(data);
            return head;
        }
        while (index - 1 > 0) {
            temp = temp->next;
            index -= 1;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }
    return head;
}

struct Node * insEnd(int data) {
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node *temp = head;
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = newNode;
    }
    return head;
}

int main() {
	head = insBeg(5);
	head = insBeg(4);
	head = insBeg(3);
	head = insBeg(2);
	head = insEnd(9);
	head = insEnd(11);
	head = insPos(7, 4);
	head = insPos(0, 0);
	printLL(head);
}
