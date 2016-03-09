#include "matrix.hpp"

int main() {
    const unsigned matrixSize = 5;
    vector<TYPE> Vector;
    generateRandomVector(matrixSize, Vector);
    printVector(Vector);
    return 0;
}
