#include "matrix.hpp"

int main() {
    int matrixSize = 100;
    vector<vector<TYPE> > Matrix;
    Matrix.resize(matrixSize);

    vector<TYPE> X;
    generateRandomVector(matrixSize, X);
    printVector(X);
    cout << endl;
    cout << calculateVectorNorm(X) << endl;
    cout << endl;
    cout << endl;
    insertDataToMatrix(matrixSize, Matrix);
    printMatrix(Matrix);

    cout << endl;
    cout << endl;

    vector<TYPE> Vector;
    multiplyMatrixByVector(matrixSize, Matrix, X, Vector);
    vector<TYPE> solution = gaussianElimination(matrixSize, Matrix, Vector);

    printVector(solution);
    cout << endl;
    cout << calculateVectorNorm(solution) << endl;

    return 0;
}
