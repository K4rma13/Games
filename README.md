# Games
Just some random games in different languages

## Snake game in C
Works much better than i anticipated, the most important thing i learned 
from this one was how to use a child process to get the keystrokes directly and without making the game stop while waitting for input

## Maze things
I started just by making a [maze generator](https://github.com/K4rma13/Games/tree/master/mazeGen) with a dfs algorithm to test draw routines i made with the *curses* library in python, then i tought "Well i can pretty easily make this into a [2d game](https://github.com/K4rma13/Games/tree/master/mazeGame) which i was right it was easy, but it was easy to solve as well so i though "Well it wouldnt be that easy if i was really in the maze" and then i got the idea of implementing a [wolfenstein style game](https://github.com/K4rma13/Games/tree/master/fpsMaze) with a raycaster engine 
### Maze Generator
Its a simple implementation of a dfs algorithm with some drawing routines i made using *curses* to create some pretty cool looking and sometimes complex mazes and i love how such a simple algorithm can create that
### Maze Game
Using the [maze generator](https://github.com/K4rma13/Games/tree/master/mazeGen) i just added controls _w a s d_ to control a green square in the maze also some colision detection and it was ready in like 5 min
### Maze FPS
Well after spending 5 min in the [2d game maze game](https://github.com/K4rma13/Games/tree/master/mazeGame) and being able to solve it with ease i came with the not so bright idea of upping the difficulty by making the game a fps(i mean without the shooting so probably just and fp?) i had an idea of the raycasting technic to emulate 3D spaces using a 2D environment but my trigonometry was not quite there so i spent some good hours just drawing and deducing some equations but after some headaches it worked and depending on the maze size it was quite challenging, but i can still add a menu to chose the maze size
