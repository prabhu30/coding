#include<stdio.h>
int main(){
	int n,t;
	scanf("%d",&n);
	t=n;
	n=(n*2)-2;
	for(int i=0;i<t;i++){
		for(int j=0;j<=n;j++){
			if(i==0){
				printf("*");
			}
			else if(i==j || i+j==n){
				printf("*");
			}
			else{
				printf(" ");
			}
		}
		printf("\n");
	}
}
