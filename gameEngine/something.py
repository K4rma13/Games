#! /usr/bin/python3

from math import cos, sin, pi
import curses
from curses import wrapper
import subprocess


def refresh():
	stdscr.refresh()
	stdscr.erase()

def drawCircle(a,b,r,color):
	for i in range(y):
		for j in range(x):
			if (j-a)**2 + (i-b)**2 <= r*r+r and (j-a)**2 + (i-b)**2 >= r*r-r:
				stdscr.addch(i,j," ",color)

def drawLine(x1,y1,x2,y2,color):
	a=y1-y2
	b=x2-x1
	dist = a*a+b*b
	c=x1*y2-x2*y1
	xmax = round(max(x1,x2))
	xmin = round(min(x1,x2))
	ymax = round(max(y1,y2))
	ymin = round(min(y1,y2))
	for i in range(ymin,ymax+1):
		for j in range(xmin,xmax+1):
			if ((a*j+b*i+c)**2 <= dist/2):
				stdscr.addch(i,j," ",color)

def drawLineAngle(x1,y1,d,a,color):
	x2=cos(pi*a)*d + x1
	y2=sin(pi*(-a))*d + y1
	drawLine(x1,y1,x2,y2,color)

def drawSquare(x1,y1,x2,y2,color):
	xmax = max(x1,x2)
	xmin = min(x1,x2)
	ymax = max(y1,y2)
	ymin = min(y1,y2)
	for i in range(ymin,ymax):
		for j in range(xmin,xmax):
			stdscr.addch(i,j," ",color)


x=70
y=70


stdscr = curses.initscr()
curses.curs_set(0)
curses.start_color()
curses.use_default_colors()
curses.init_color(1,1000,1000,1000)
curses.init_pair(1,-1,1)
white = curses.color_pair(1)
k=0
g=0
l=0
while(1):
	drawCircle(25,25,l,white)
	drawLineAngle(25,25,l,k,white)
	refresh()
	k-= 1 / 24
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
