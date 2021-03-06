#! /usr/bin/python3

from math import cos, sin, pi
import curses
from curses import wrapper
import subprocess
from random import randrange

x=91
y=91


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
	c=x1*y2-x2*y1
	xmax = max(x1,x2)
	xmin = min(x1,x2)
	ymax = max(y1,y2)
	ymin = min(y1,y2)
	for i in range(ymin,ymax+1):
		for j in range(xmin,xmax+1):
			if (a*j+b*i+c <= 0+10 and a*j+b*i+c >= 0-9):
				stdscr.addch(i,j," ",color)

def drawLineAngle(x1,y1,d,a,color):
	x2=cos(pi*a)*d + x1
	y2=sin(pi*(-a))*d + y1
	drawLine(x1,y1,x2,y2)

def drawSquare(x1,y1,x2,y2,color):
	xmax = max(x1,x2)
	xmin = min(x1,x2)
	ymax = max(y1,y2)
	ymin = min(y1,y2)
	for i in range(ymin,ymax):
		for j in range(xmin,xmax):
			stdscr.addch(i,j," ",color)

class quadrado:
	x=0
	y=0
	s=4
	lef=True
	rig=True
	top=True
	bot=True
	visited=False
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def draw(self):
		if self.top:
			drawLine(self.x,self.y,self.x+self.s,self.y,white)
		if self.lef:
			drawLine(self.x,self.y,self.x,self.y+self.s,white)
		if self.bot:
			drawLine(self.x,self.y+self.s,self.x+self.s,self.y+self.s,white)
		if self.rig:
			drawLine(self.x+self.s,self.y,self.x+self.s,self.y+self.s,white)

class pos:
	x=0
	y=0
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def draw(self):
		ay=self.y*4+1
		ax=self.x*4+1
		drawSquare(ax,ay,ax+3,ay+3,green)

def goTo(x2,y2):
	if y2>=0 and y2<22 and x2>=0 and x2<22 and not quadrados[y2][x2].visited :
		stack.append(pos(p.x,p.y))
		quadrados[y2][x2].visited=True
		if y2-p.y == 1:
			quadrados[y2][x2].top=False
			quadrados[p.y][p.x].bot=False
		elif y2-p.y == -1:
			quadrados[y2][x2].bot=False
			quadrados[p.y][p.x].top=False
		elif x2-p.x == 1:
			quadrados[y2][x2].lef=False
			quadrados[p.y][p.x].rig=False
		elif x2-p.x == -1:
			quadrados[y2][x2].rig=False
			quadrados[p.y][p.x].lef=False
		p.x=x2
		p.y=y2
		return True
	else:
		return False


stdscr = curses.initscr()
curses.curs_set(0)
stdscr.idcok(False)
stdscr.idlok(False)
curses.start_color()
curses.init_color(0,0,0,0)
curses.init_color(1,1000,1000,1000)
curses.init_pair(1,0,1)
white = curses.color_pair(1)
curses.init_pair(2,1,0)
black = curses.color_pair(2)
curses.init_color(2,0,1000,0)
curses.init_pair(3,0,2)
green = curses.color_pair(3)
while True:
	quadrados = [[quadrado(xq,yq) for xq in range(0,88,4)] for yq in range(0,88,4) ]
	startx = 0
	starty = 0
	p = pos(startx,starty)
	stack = [ pos(startx,starty) ]
	quadrados[starty][startx].visited=True
	while stack:
		for qlinha in quadrados:
			for q in qlinha:
				q.draw()
		p.draw()
		refresh()
		k = randrange(4)
		if k==0:
			if not (goTo(p.x,p.y-1) or goTo(p.x+1,p.y) or goTo(p.x-1,p.y) or goTo(p.x,p.y+1) ):
				p = stack.pop()
		elif k==1:
			if not (goTo(p.x-1,p.y) or goTo(p.x,p.y-1) or goTo(p.x+1,p.y) or goTo(p.x,p.y+1)):
				p = stack.pop()
		elif k==2:
			if not (goTo(p.x,p.y+1) or goTo(p.x+1,p.y) or goTo(p.x-1,p.y) or goTo(p.x,p.y-1)):
				p = stack.pop()
		elif k==3:
			if not ( goTo(p.x-1,p.y) or goTo(p.x,p.y-1) or goTo(p.x,p.y+1) or goTo(p.x+1,p.y)):
				p = stack.pop()
		#subprocess.run(['sleep','0.05'])
	subprocess.run(['sleep','1'])

stdscr.getch()
curses.endwin()
