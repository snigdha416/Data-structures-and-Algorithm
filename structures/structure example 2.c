#include<stdio.h>

struct Employee {
	int id;
	float salary;
	char name[20];
};

int main() {
	struct Employee emp = {123, 80000.00, "Ram"};
	printf("%d %f %s\n", emp.id, emp.salary, emp.name);
	printf("%d", sizeof(struct Employee));
}
