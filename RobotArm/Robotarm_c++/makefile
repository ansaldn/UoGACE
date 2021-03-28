CC=g++
CFLAGS = -I.
LIBS=-lusb -lncurses

all: robot.cpp
	$(CC) -o robot Robot_controller.cpp arm.cpp $(CFLAGS) $(LIBS)
