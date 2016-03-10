CXX = g++
FLAGS = -Wall -pedantic
DEPS = matrix.hpp
OBJ = main.o matrix.o

all: compile clean

compile: $(OBJ)
	$(CXX) $(FLAGS) -o main $(OBJ)

main.o: $(DEPS) main.cpp
	$(CXX) $(FLAGS) -o main.o -c main.cpp

matrix.o : $(DEPS) matrix.cpp
	$(CXX) $(FLAGS) -o matrix.o -c matrix.cpp

clean:
	rm -f *.o
