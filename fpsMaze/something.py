#! /usr/bin/python3

from math import cos, sin, pi, floor, atan
import curses
from curses import wrapper
import subprocess
from random import randrange

x=180
y=91


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
			else:
				stdscr.addch(i,j,plane[i][j],curses.color_pair(2))
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


plane = [[" " for cols in range(x)] for rows in range(y)] 

stdscr = curses.initscr()
stdscr.idcok(False)
stdscr.idlok(False)
curses.noecho()
curses.start_color()
curses.init_color(0,0,0,0)
curses.init_color(1,900,900,900)
curses.init_pair(1,0,1)
curses.init_pair(2,1,0)

curses.init_color(2,700,700,700)
curses.init_color(3,500,500,500)
curses.init_color(4,300,300,300)
curses.init_pair(4,0,2)
curses.init_pair(5,0,3)
curses.init_pair(6,0,4)

curses.init_color(4,300,300,300)
curses.init_pair(7,0,5)

curses.init_color(5,0,1000,0)
curses.init_pair(3,0,5)
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
def edgesAux(x1,y1):
	minimo=(x1-player.x)**2+(y1-player.y)**2
	bestx=x1
	besty=y1
	for ky in range(2):
		for kx in range(2):
			if((x1+kx-player.x)**2+(y1+ky-player.y)**2<minimo):
				minimo=(x1+kx-player.x)**2+(y1+ky-player.y)**2
				bestx=x1+kx
				besty=y1+ky
	if bestx==player.x:
		return 500
	a = atan((besty-player.y)/(bestx-player.x))
	if bestx-player.x<0:
		a=a+pi
	return a


def povDraw():
	c=0
	for angle in range(-45,45):
		green=False
		pixels2=0
		edge=False
		white=False
		dgray=False
		gray=False
		lgray=False
		for d in range(0,1200,1):
			d1 = d/100
			if maze[floor(d1*sin((angle/180+player.a)*pi)+player.y)][floor(d1*cos((angle/180+player.a)*pi)+player.x)]=="X":
				#edges
				xqa=floor(d1*cos((angle/180+player.a)*pi)+player.x)
				yqa=floor(d1*sin((angle/180+player.a)*pi)+player.y)
				edgeA = edgesAux(xqa,yqa)
				if edgeA-0.02 <= (angle/180+player.a)*pi <= edgeA+0.02:
					edge=True
				#coloring
				if floor(d1*sin((angle/180+player.a)*pi)+player.y) >80 and floor(d1*cos((angle/180+player.a)*pi)+player.x) > 80 and ((floor(d1*sin((angle/180+player.a)*pi)+player.y)%2 or floor(d1*sin((angle/180+player.a)*pi)+player.y))%2):
					green=True
				rd = d1*sin(pi/2-abs(angle/180+player.a))
				if d1<3:
					white=True
				elif d1<6:
					lgray=True
				elif d1<9:
					gray=True
				else:
					dgray=True
				pixels2 = floor((100-(rd/12*70+20))/2)
				break
		for size in range(-pixels2,pixels2):
			if green:
				plane[size+52][c]="Y"
				plane[size+52][c+1]="Y"
			elif edge:
				plane[size+52][c]="#"
				plane[size+52][c+1]="#"
			elif white:
				plane[size+52][c]="X"
				plane[size+52][c+1]="X"
			elif dgray:
				plane[size+52][c]="J"
				plane[size+52][c+1]="J"
			elif gray:
				plane[size+52][c]="H"
				plane[size+52][c+1]="H"
			elif lgray:
				plane[size+52][c]="G"
				plane[size+52][c+1]="G"
		c+=2

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
subprocess.run(['sleep','2'])

while 1:
	for j in range(57,y):
		for i in range(x):
			if j>70:
				plane[j][i]="x"
			else:
				plane[j][i]="."

	povDraw()
	refresh()
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
