CXX = g++
FLAGS = -Wall -pedantic -std=c++11
DEPS = matrix.hpp
OBJ = main.o matrix.o

all: compile clean

compile: $(OBJ)
	$(CXX) $(FLAGS) -o main $(OBJ)

main.o: $(DEPS) main.cpp
	$(CXX) $(FLAGS) -o main.o -c main.cpp

matrix.o : $(DEPS) matrix.cpp
	$(CXX) $(FLAGS) -o matrix.o -c matrix.cpp

generatetestsfordouble: main.o matrix.o compile
	bash scriptzad1.sh


clean:
	rm -f *.o
