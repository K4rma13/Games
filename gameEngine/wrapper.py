import subprocess

def screenSize(x,y):
	subprocess.run(['xfce4-terminal',f'--geometry={x}x{y}+50+50','-x','./something.py'])

screenSize(90,90)