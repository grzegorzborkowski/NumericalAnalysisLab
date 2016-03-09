CXX = g++
FLAGS = -Wall -pedantic
DEPS = matrix.hpp
OBJ = main.o matrix.o

%.o: %.c $(DEPS)
	$(CXX) $(FLAGS) -c -o $@ @ $< -I.

main: $(OBJ)
	$(CXX) $(FLAGS) -o $^ -I.

clean:
	rm -f *.o
