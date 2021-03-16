CC=g++
CFLAGS = -I.
LIBS=-lusb -lncurses

all: robot.cpp
	$(CC) -o robot robot.cpp robotarm.cpp $(CFLAGS) $(LIBS)
