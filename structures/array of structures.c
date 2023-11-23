#include<stdio.h>

struct Employee {
	int id;
	float salary;
	char name[20];
};

int main() {
	struct Employee emp[3];
	int i;
	for(i = 0; i < 3; i++) {
		scanf("%d %f %s", &emp[i].id, &emp[i].salary, emp[i].name);
	}
	for(i = 0; i < 3; i++) {
		printf("%d %f %s\n", emp[i].id, emp[i].salary, emp[i].name);
	}
}
