#include <stdio.h>

int main(){
	int num;
	scanf("%d", &num);
	int a[num];
	long int mul=1;
	for(int i=0;i<num;i++){
		scanf("%d",&a[i]);
	}
	for(int i=0;i<num;i++){
		mul=(mul*a[i])%1000000007;
	}
	printf("%d",mul);
	

}
