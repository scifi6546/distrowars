CC=g++
LIBS=-lncurses
CFLAGS=-I -w -ggdb
main: main.cpp
	$(CC) $(CFLAGS) -c main.cpp -o main.o
	$(MAKE) window
	$(CC) $(CFLAGS) main.o window.o -o out $(LIBS)
run:
	$(MAKE) main
	./out
window: window.cpp
	$(CC) -c $(CFLAGS) window.cpp -o window.o
debug:
	$(MAKE) main
	gdb out
all:
	$(MAKE) main
