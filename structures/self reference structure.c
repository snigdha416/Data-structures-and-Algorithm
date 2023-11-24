#include<stdio.h>

struct Employee {
	int id;
	float salary;
	char name[20];
};

int main() {
	struct Employee *empPtr, emp;
	empPtr = &emp;
	scanf("%d", &empPtr->id);
	printf("%d %d %d %d", empPtr->id, emp.id, 
					&empPtr->id, *(&empPtr->id));
}
