snake: plane.o main.o snake.o
	gcc plane.o main.o snake.o -o snake
plane.o: plane.c plane.h
	gcc plane.c -c -o plane.o
main.o: main.c
	gcc main.c -c -o main.o
snake.o: snake.c snake.h
	gcc snake.c -c -o snake.o

clean:
	rm main.o plane.o snake.o
