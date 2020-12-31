#include <stdio.h>
#include <stdlib.h>

typedef struct locals {
	char username[50];
	char role[10];
} locals;

int main(void) {
	locals config;
	strcpy(config.role, "user");

	setbuf(stdout, NULL);

	printf("Enter your name: ");
	scanf("%s", config.username);

	printf("Hello, %s!\n", config.username);
	printf("Role: %s\n", config.role);


	if (strcmp(config.role, "admin") == 0) {
		printf("Flag: %s\n", getenv("FLAG"));
	} else {
		puts("Access denied.");
	}
}