#include<stdio.h>

struct Employee {
	int id;
	float salary;
	char name[20];
};

int main() {
	struct Employee emp = {123, 80000.00, "Ram"};
	struct Employee emp1, emp2;
	scanf("%d %f %s", &emp1.id, &emp1.salary, &emp1.name);
	scanf("%d %f %s", &emp2.id, &emp2.salary, &emp2.name);
	
	printf("%d %f %s\n", emp.id, emp.salary, emp.name);
	printf("%d %f %s\n", emp1.id, emp1.salary, emp1.name);
	printf("%d %f %s", emp2.id, emp2.salary, emp2.name);
}
