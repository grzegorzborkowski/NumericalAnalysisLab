CXX = g++
FLAGS = -Wall -pedantic
DEPS = matrix.hpp
OBJ = main.o matrix.o

all: matrix.o clean

%.o: %.cpp $(DEPS)
	$(CXX) $(FLAGS) -c -o $@ $< -I.

matrix: $(OBJ)
	$(CXX) $(FLAGS) -o $@ $^ -I.

clean:
	rm -f *.o
