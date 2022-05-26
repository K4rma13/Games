#include "plane.h"

char** createPlane(int m, int n){
	char** plane = malloc(sizeof(char *) * m);
	for(int i=0; i<m;i++){
		plane[i] = malloc(n);
	}
	return plane;
}

void resetPlane(char** plane, int m, int n){
	for(int i=0; i<m;i++){
		for(int j=0; j<n;j++){
			if(j==0||j==n-1||i==0||i==m-1){
				plane[i][j]=1;
			}
			else{
				plane[i][j]=0;
			}
		}
	}
}

void printPlane(char** plane, int m, int n, SNAKE* s){
	printf("\x1b[0;0H");
	printf("\x1b[0J");
	for(int i=0; i<m;i++){
		for(int j=0; j<n;j++){
			if(plane[i][j]==1){
				printf("\x1b[48;2;0;255;0m \x1b[0m");
			}
			else if(plane[i][j]==2){
				printf("\x1b[48;2;255;0;0m \x1b[0m");
			}
			else if(plane[i][j]==3){
				printf("\x1b[48;2;255;150;0m \x1b[0m");
			}
			else if(plane[i][j]==4){
				printf("\x1b[48;2;0;120;230m \x1b[0m");
			}
			else{
				printf(" ",plane[i][j]);
			}
			//printf("%d",plane[i][j]);
		}
		printf("\n");
		
	}
	printf("\x1b[30;48;2;221;216;196mSize: %d\n\x1b[0m\x1b[?25l\x1b[30m\n",s->size);
}

void drawFood(FOOD* f, char** plane,int m, int n){
	plane[f->x][f->y]=4;
}


void drawSnake(SNAKE* s, char** plane,int m, int n){
	int y,x;
	LPonto head = s->pontos;
	drawBody(head->next,plane,m,n);
	if((head->y)<=0){
		head->y=n-2;
	}
	y=((head->y)%(m-2))+1;
	if((head->x)<=0){
		head->x=m-2;
	}
	x=((head->x)%(n-2))+1;
	plane[y][x]=3;
}

void drawBody(LPonto s, char** plane,int m, int n){
	int y,x;
	if((s->y)<=0){
		s->y=n-2;
	}
	y=((s->y)%(m-2))+1;
	if((s->x)<=0){
		s->x=m-2;
	}
	x=((s->x)%(n-2))+1;
	plane[y][x]=2;
	if(s->next!=NULL){
		drawBody(s->next,plane,m,n);
	}
}

void gameOver(int m, int n, char** plane,SNAKE* s){
	printf("\x1b[0;0H");
	printf("\x1b[0J");
	for(int i=0; i<m;i++){
		for(int j=0; j<n;j++){
			if(plane[i][j]==1){
				printf("\x1b[48;2;0;255;0m \x1b[0m");
			}
			else if(plane[i][j]==2){
				printf("\x1b[48;2;255;0;255m \x1b[0m");
			}
			else if(plane[i][j]==3){
				printf("\x1b[48;2;250;70;0m \x1b[0m");
			}
			else if(plane[i][j]==4){
				printf("\x1b[48;2;0;120;230m \x1b[0m");
			}
			else{
				printf(" ",plane[i][j]);
			}
			//printf("%d",plane[i][j]);
		}
		printf("\n");
		
	}
	int y=m/2-1,x;
	if(n/2-7>0){
		x=n/2-6;
	}
	else{
		x=0;
	}
	printf("\x1b[%d;%dH",y,x);
	printf("\x1b[30;48;2;221;216;196m===============\n");
	printf("\x1b[%d;%dH",y+1,x);
	printf("\x1b[30;48;2;221;216;196m   GAME OVER   \n");
	printf("\x1b[%d;%dH",y+2,x);
	printf("\x1b[30;48;2;221;216;196m   Score:%3d   \n",s->size);
	printf("\x1b[%d;%dH",y+3,x);
	printf("\x1b[30;48;2;221;216;196m===============\n");
	printf("\x1b[%d;%dH\x1b[0m\x1b[30m",m+5,n);
	getchar();
	exit(1);
}