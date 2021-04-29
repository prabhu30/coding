#include <stdio.h>

int main(){
	int t;
	scanf("%d", &t);
	for(int i=0;i<t;i++){
		int g,p,n,psum=0,gsum=0;
		scanf("%d %d\n",&g,&p);
		scanf("%d\n",&n);
		for(int j=0;j<n;j++){
			if(i%2==0){
				int gg,pp;
			scanf("%d %d",&gg,&pp);
			psum=psum+(gg*g);
			gsum=gsum+(pp*p);
			}
			else{
				int gg,pp;
			scanf("%d %d",&gg,&pp);
			psum=psum+(gg*p);
			gsum=gsum+(pp*g);
			}
		}
		printf("%d\n",psum+gsum);
	}
}
