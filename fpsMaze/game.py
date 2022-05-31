#! /usr/bin/python3

import subprocess

def screenSize(x,y):
	subprocess.run(['xfce4-terminal',f'--geometry={x}x{y}+50+50','--title=FPSMaze','-x','./something.py'])

screenSize(490,245)