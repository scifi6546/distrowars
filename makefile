CC=g++
LIBS=-lSDL2 -lGLEW  -lGL
CFLAGS=-I -w -ggdb
main: main.cpp game_engine.cpp
	$(CC) $(CFLAGS) main.c -o main.o
	$(CC) $(CFLAGS) main.o window.o -o out $(LIBS)
run:
	$(MAKE) main
	./out
window: window.cpp
	$(CC) -c $(CFLAGS) window.cpp -o window.o
debug:
	$(MAKE) main
	optirun gdb out
all:
	$(MAKE) main
