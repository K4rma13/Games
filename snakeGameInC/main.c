#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <signal.h>
#include <errno.h>
#include <linux/input.h>
#include <string.h>
#include <stdio.h>
#include "plane.h"
#include "snake.h"

int newdata=0;

void sig_usr(int signo){
    newdata=1;
    return;
}


#define STDIN 0


void keyboard(SNAKE* s, int code){
	//a=30 w=17 d=32 s=31
	if(code==30&&s->dir!=RIGHT){
		s->dir=LEFT;
	}
	else if(code==17&&s->dir!=DOWN){
		s->dir=UP;
	}
	else if(code==32&&s->dir!=LEFT){
		s->dir=RIGHT;
	}
	else if(code==31&&s->dir!=UP){
		s->dir=DOWN;
	}
	else if(code==57){
		s->ateFood=true;
	}
	else if(code==16){
		exit(1);
	}
}


int main(){
	int m = 15, n = 15;
	int x=5,y=5;

	SNAKE* s = malloc(sizeof(SNAKE));
	FOOD* f = malloc(sizeof(FOOD));
	
	srand(time(NULL));
	
	pid_t prntid = getpid();
	pid_t pid;
	int pipek[2];
	pipe(pipek);
	//Child process handles keystrokes
	if((pid=fork())==0){
		//Keyboard buffer path
		const char *dev = "/dev/input/event0";
		struct input_event ev;
		int fd;
	
		fd = open(dev, O_RDONLY);
		if (fd == -1) {
			fprintf(stderr, "Cannot open %s: %s.\n", dev, strerror(errno));
			return EXIT_FAILURE;
		}

		int code;
		while(1){
			//reads from keyboard pipe
			read(fd, &ev, sizeof ev);
			if(ev.type == EV_KEY && ev.value==1 && (ev.code==16 || ev.code==57 || ev.code==31 || ev.code==30 || ev.code==32 || ev.code==17)){
				//Sends term signal to parent process when a key is pressed and sends the pressed key code thro a pipe
				kill(prntid, SIGTERM);
				code = (int)ev.code;
				write(pipek[1], &code, sizeof(int));
			};
		}
	}
	else{ //Parent process contains the actual game
		float time=0.1;
		char* sleepAmmount= malloc(50);
		signal(SIGTERM,sig_usr);
		char in=0;
		char** plane = createPlane(m,n);
		int keypress;
		createFood(f,m,n);
		setSnake(s,x,y,RIGHT);
		do{
			if(newdata){
				read(pipek[0], &keypress, sizeof(int));
				keyboard(s,keypress);
				newdata=0;
			}
			updateSnake(s);
			resetPlane(plane,m,n);
			snakeAte(s,f,m,n);
			drawSnake(s,plane,m,n);
			drawFood(f,plane,m,n);
			printPlane(plane,m,n,s);
			increaseSpeed(s,&time);
			sprintf(sleepAmmount,"sleep %f",time);
			system(sleepAmmount);
	
			if(snakeDead(s,m,n)){
				gameOver(m,n,plane,s);
			}
		}while(in!='q');
	}
	return 1;
}