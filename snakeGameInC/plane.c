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

void printPlane(char** plane, int m, int n){
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
}

void drawFood(FOOD* f, char** plane,int m, int n){
	plane[f->x][f->y]=4;
	plane[f->x+1][f->y]=4;
	plane[f->x][f->y+1]=4;
	plane[f->x+1][f->y+1]=4;
}


void drawSnake(SNAKE* s, char** plane,int m, int n){
	int y,x;
	LPonto head = s->pontos;
	if((head->y)<=0){
		head->y=n-2;
	}
	y=((head->y)%(m-2))+1;
	if((head->x)<=0){
		head->x=m-2;
	}
	x=((head->x)%(n-2))+1;
	plane[y][x]=3;
	drawBody(head->next,plane,m,n);
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

void gameOver(int m, int n){
	int y=m/2,x=n/2-9;
	printf("\x1b[%d;%dH",y,x);
	printf("\x1b[30;48;2;221;216;196m====================\n");
	printf("\x1b[%d;%dH",y+1,x);
	printf("\x1b[30;48;2;221;216;196m     GAME OVER      \n");
	printf("\x1b[%d;%dH",y+2,x);
	printf("\x1b[30;48;2;221;216;196m====================\n");
	getchar();
	exit(1);
}