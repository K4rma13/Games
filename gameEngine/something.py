#! /usr/bin/python3

from math import cos, sin, pi
import curses
from curses import wrapper
import subprocess


def refresh():
	stdscr.clear()
	for i in range(y):
		for j in range(x):
			stdscr.addch(i,j,plane[i][j])
			plane[i][j]=" "
	stdscr.refresh()

def drawCircle(a,b,r):
	for i in range(y):
		for j in range(x):
			if (j-a)**2 + (i-b)**2 <= r*r+r and (j-a)**2 + (i-b)**2 >= r*r-r:
				plane[i][j]="X"

def drawLine(x1,y1,x2,y2):
	a=y1-y2
	b=x2-x1
	c=x1*y2-x2*y1
	for i in range(y):
		for j in range(x):
			if (a*j+b*i+c <= 0+10 and a*j+b*i+c >= 0-9) and j <= max(x1,x2) and j >= min(x1,x2) and i <= max(y1,y2) and i >= min(y1,y2):
				plane[i][j]="X"

def drawLineAngle(x1,y1,d,a):
	x2=cos(pi*a)*d + x1
	y2=sin(pi*(-a))*d + y1
	drawLine(x1,y1,x2,y2)


x=70
y=70

plane = [[" " for cols in range(x)] for rows in range(y)] 

stdscr = curses.initscr()
k=0
g=0
l=0
while(1):
	drawCircle(25,25,l)
	drawLineAngle(25,25,l,k)
	refresh()
	k-=0.03
	if l==0:
		g=0
	elif l==25:
		g=1
	if g:
		l-=1
	else:
		l+=1
	subprocess.run(['sleep','0.2'])
stdscr.getch()
curses.endwin()
