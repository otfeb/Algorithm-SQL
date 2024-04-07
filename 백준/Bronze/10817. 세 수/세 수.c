#include <stdio.h>

int main(){

    int a[3], change = 0;
	for (int i = 0; i < 3; i++) {
		scanf("%d", a + i);
	}
	for (int i = 0; i < 3; i++) {
		for (int j = i + 1; j < 3; j++) {
			if (a[i] > a[j]) {
				change = a[i];
				a[i] = a[j];
				a[j] = change;
			}
		}
	}
	printf("%d", a[1]);
	return 0;
}