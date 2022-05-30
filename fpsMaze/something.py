#! /usr/bin/python3

from math import sin, pi, floor, sqrt, acos, atan, cos
import curses
from curses import wrapper
import subprocess
from random import randrange

x=180
y=91
mX=5
mY=5

def refresh():
	for i in range(y):
		for j in range(x):
			if plane[i][j]== "X":
				stdscr.addch(i,j," ",curses.color_pair(1))
			elif plane[i][j]== "G":
				stdscr.addch(i,j," ",curses.color_pair(4))
			elif plane[i][j]== "H":
				stdscr.addch(i,j," ",curses.color_pair(5))
			elif plane[i][j]== "J":
				stdscr.addch(i,j," ",curses.color_pair(6))
			elif plane[i][j]== "Y":
				stdscr.addch(i,j," ",curses.color_pair(3))
			elif plane[i][j]== "#":
				stdscr.addch(i,j," ",curses.color_pair(7))
			else:
				stdscr.addstr(i,j,plane[i][j],curses.color_pair(2))
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
	xmax = max(x1,x2)
	xmin = min(x1,x2)
	ymax = max(y1,y2)
	ymin = min(y1,y2)
	for i in range(ymin,ymax+1):
		for j in range(xmin,xmax+1):
			if (a*j+b*i+c <= 0+10 and a*j+b*i+c >= 0-9):
				plane[i][j]="X"

def drawLineAngle(x1,y1,d,a):
	x2=cos(pi*a)*d + x1
	y2=sin(pi*(-a))*d + y1
	drawLine(x1,y1,x2,y2)


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
			drawLine(self.x,self.y,self.x+self.s,self.y)
		if self.lef:
			drawLine(self.x,self.y,self.x,self.y+self.s)
		if self.bot:
			drawLine(self.x,self.y+self.s,self.x+self.s,self.y+self.s)
		if self.rig:
			drawLine(self.x+self.s,self.y,self.x+self.s,self.y+self.s)

class pos:
	x=0
	y=0
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def draw(self):
		ay=self.y*4+1
		ax=self.x*4+1
		for j in range(3):
			for i in range(3):
				plane[j+ay][ax+i]="Y"

def goTo(x2,y2):
	if y2>=0 and y2<mY and x2>=0 and x2<mX and not quadrados[y2][x2].visited :
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


plane = [[" " for cols in range(x)] for rows in range(y)] 

stdscr = curses.initscr()
stdscr.idcok(False)
stdscr.idlok(False)
curses.noecho()
curses.start_color()
curses.init_color(0,0,0,0)
curses.init_color(1,800,800,800)
curses.init_pair(1,0,1)
curses.init_pair(2,1,0)

#Gray color
curses.init_color(2,700,700,700)
curses.init_color(3,500,500,500)
curses.init_color(4,300,300,300)
curses.init_pair(4,0,2)
curses.init_pair(5,0,3)
curses.init_pair(6,0,4)

#Edge color
curses.init_color(6,400,400,420)
curses.init_pair(7,4,6)

curses.init_color(5,0,700,100)
curses.init_pair(3,0,5)
quadrados = [[quadrado(xq,yq) for xq in range(0,mX*4,4)] for yq in range(0,mY*4,4) ]
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
	if len(stack)==1:
		maze = [[plane[j][i] for i in range(x)] for j in range(y)]
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
	#subprocess.run(['sleep','0.01'])


class Edges:
	x=0
	y=0
	d=0
	def __init__(self,x,y,d):
		self.x=x
		self.y=y
		self.d=d
def getDist(e):
	return e.d


def edgesAux(x1,y1):
	if (x1%1 < 0.1 or x1%1>0.9) and (y1%1 < 0.1 or y1%1>0.9):
		return True
	return False


def povDraw():
	c=0
	for angle in range(-90,90):
		green=False
		pixels2=0
		edge=False
		white=False
		dgray=False
		gray=False
		lgray=False
		#for d in range(0,1200,10):
		#	d1 = d/100
		aAngle = (angle/540+player.a)*pi
		dirX = cos(aAngle)
		dirY = sin(aAngle)
		if dirX == 0:
			stepSizex = 900000
			stepSizey = 1
		else:
			stepSizex= sqrt(1+(dirY/dirX)*(dirY/dirX))
		if dirY == 0:
			stepSizey = 900000
			stepSizex = 1
		else:
			stepSizey= sqrt(1+(dirX/dirY)*(dirX/dirY))
		mapcheckX = floor(player.x)
		mapcheckY = floor(player.y)
		
		if dirX < 0:
			stepX = -1
			distX = (player.x - mapcheckX) * stepSizex
		else:
			stepX = 1
			distX = (mapcheckX+1 - player.x) * stepSizex
		if dirY < 0:
			stepY = -1
			distY = (player.y - mapcheckY) * stepSizey
		else:
			stepY = 1
			distY = (mapcheckY+1 - player.y) * stepSizey
		dist=0
		foundWall=False
		while dist<20 and not foundWall:
			if(distY>distX):
				mapcheckX+= stepX
				dist=distX
				distX+= stepSizex
				
			else:
				mapcheckY+= stepY
				dist=distY
				distY+= stepSizey
				
			#if mapcheckX>=0 and mapcheckX<mX and mapcheckY>=0 and mapcheckY<mY:
			if maze[mapcheckY][mapcheckX]=="X":
				foundWall=True

		if foundWall:
			#edges
			d1 = dist
			xqa=d1*cos(aAngle)+player.x
			yqa=d1*sin(aAngle)+player.y
			if edgesAux(xqa,yqa):
				edge=True
			#coloring
			if floor(d1*sin(aAngle)+player.y) >mY*4-8 and floor(d1*cos(aAngle)+player.x) > mX*4-8 and ((floor(d1*sin(aAngle)+player.y)%2 or floor(d1*sin(aAngle)+player.y))%2):
				green=True
			rd = abs(d1*cos(angle/540*pi))
			if d1<3:
				white=True
			elif d1<6:
				lgray=True
			elif d1<9:
				gray=True
			else:
				dgray=True
			#pixels2 = floor((90-(rd/20*90))/2)
			#pixels2= floor((90-rd*4)/2)
			if rd<1:
				rd=1
			pixels2= round(90/rd)
			#stdscr.addstr(floor(c/2),0,f'{rd}')
		
		for size in range(-pixels2,pixels2):
			center=47
			height=size+center
			if height>90:
				height=90
			if height<0:
				height=0
			if green:
				plane[height][angle+90]="Y"
			elif edge:
				plane[height][angle+90]="#"
			elif white:
				plane[height][angle+90]="X"
			elif dgray:
				plane[height][angle+90]="J"
			elif gray:
				plane[height][angle+90]="H"
			elif lgray:
				plane[height][angle+90]="G"

class Player:
	x=0
	y=0
	angle=1
	a=0
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def walk(self,d):
		self.x+= d*cos(self.a*pi)
		self.y+= d*sin(self.a*pi)

player = Player(2,2)
subprocess.run(['sleep','0.5'])

while 1:
	for j in range(57,y):
		for i in range(x):
			if j>70:
				plane[j][i]="x"
			else:
				plane[j][i]="."
	#stdscr.clear()
	povDraw()
	refresh()
	stdscr.addstr(0,30,f'x:{player.x} y:{player.y} Angle:{player.a}')

	stdscr.refresh()
	key = stdscr.getkey()
	if key=="a":
		player.angle-=0.05
	elif key=="w":
		player.walk(0.1)
		if maze[floor(player.y)][floor(player.x)] == "X":
			player.walk(-0.1)
	elif key=="d":
		player.angle+=0.05
	elif key=="s":
		player.walk(-0.1)
		if maze[floor(player.y)][floor(player.x)] == "X":
			player.walk(0.1)
	elif key=="q":
		player.x=86
		player.y=86
	player.a=player.angle%2-1
	
curses.endwin()
