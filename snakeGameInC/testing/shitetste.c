#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <linux/input.h>
#include <string.h>
#include <stdio.h>
#include "plane.h"
#include "snake.h"


#define STDIN 0


void keyboard(SNAKE* s, int code, int value){
	//a=30 w=17 d=32 s=31
	if(value>0 && value<=2){
		if(code==30){
			s->dir=LEFT;
		}
		else if(code==17){
			s->dir=UP;
		}
		else if(code==32){
			s->dir=RIGHT;
		}
		else if(code==31){
			s->dir=DOWN;
		}
		else if(code==16){
			exit(1);
		}
	}
}


int main(){
	int m = 15, n = 15;
	int x=5,y=5;
	SNAKE* s = malloc(sizeof(SNAKE));
	int value;
	int code;
	FILE* fd = fopen("keys","r");
	char** plane = createPlane(m,n);
	setSnake(s,x,y,RIGHT);
	do{
		fscanf(fd, "%d %d\n",value,code);
		keyboard(s,code,value);
		updateSnake(s);
		resetPlane(plane,m,n);
		drawSnake(s,plane,m,n);
		printPlane(plane,m,n);
		system("sleep 0.1");

	}while(1);
	return 1;
}