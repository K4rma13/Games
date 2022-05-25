#ifndef __PLANE_H__
#define __PLANE_H__

#include <stdio.h>
#include <stdlib.h>
#include "snake.h"

char** createPlane(int m, int n);

void resetPlane(char** plane, int m, int n);

void printPlane(char** plane, int m, int n);

void drawSnake(SNAKE* s, char** plane,int m, int n);

void drawBody(LPonto s, char** plane,int m, int n);

void drawFood(FOOD* f, char** plane,int m, int n);

void gameOver(int m, int n);

#endif