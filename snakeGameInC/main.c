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


void keyboard(SNAKE* s, struct input_event ev){
	//a=30 w=17 d=32 s=31
	if(ev.type == EV_KEY && ev.value>0 && ev.value<=2){
		if(ev.code==30&&s->dir!=RIGHT){
			s->dir=LEFT;
		}
		else if(ev.code==17&&s->dir!=DOWN){
			s->dir=UP;
		}
		else if(ev.code==32&&s->dir!=LEFT){
			s->dir=RIGHT;
		}
		else if(ev.code==31&&s->dir!=UP){
			s->dir=DOWN;
		}
		else if(ev.code==57){
			s->ateFood=true;
		}
		else if(ev.code==16){
			exit(1);
		}
	}
}


int main(){
	int m = 25, n = 25;
	int x=5,y=5;
	SNAKE* s = malloc(sizeof(SNAKE));
	FOOD* f = malloc(sizeof(FOOD));
	srand(time(NULL));
	const char *dev = "/dev/input/event0";
    struct input_event ev;
    int fd;

    fd = open(dev, O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "Cannot open %s: %s.\n", dev, strerror(errno));
        return EXIT_FAILURE;
    }


	char in=0;
	char** plane = createPlane(m,n);
	createFood(f,m,n);
	setSnake(s,x,y,RIGHT);
	do{
		read(fd, &ev, sizeof ev);
		keyboard(s,ev);
		updateSnake(s);
		resetPlane(plane,m,n);
		snakeAte(s,f,m,n);
		drawSnake(s,plane,m,n);
		drawFood(f,plane,m,n);
		printPlane(plane,m,n);
		system("sleep 0.05");
		if(snakeDead(s,m,n)){
			gameOver(m,n);
		}
	}while(in!='q');
	return 1;
}