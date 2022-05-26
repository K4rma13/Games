#ifndef __SNAKE_H__
#define __SNAKE_H__

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>



#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3

typedef struct Linkedponto{
	int x;
	int y;
	struct Linkedponto* next;
}*LPonto;

typedef struct snake{
	LPonto pontos;
	int dir;
	bool ateFood;
	int size;
}SNAKE;

typedef struct food{
	int x;
	int y;
}FOOD;


void createFood(FOOD* f,SNAKE* s,int m,int n);

void snakeAte(SNAKE* s, FOOD* f,int m,int n);

bool snakeDead(SNAKE* s,int m,int n);

void setSnake(SNAKE* s,int x, int y, int dir);

void updateSnake(SNAKE* s);

void increaseSpeed(SNAKE* s,float* time);

#endif