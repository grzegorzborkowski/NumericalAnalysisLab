#include "matrix.hpp"
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>

void generateRandomVector(int vectorSize, vector<TYPE> &Vector) {
    srand(time(NULL));
    for (int i = 0; i < vectorSize; i++) {
        int randomNumber = rand() % 2;
        if (randomNumber == 0) randomNumber = -1;
        Vector.push_back(randomNumber);
    }
}

void printVector(vector<TYPE> Vector) {
    for (int i = 0; i < Vector.size(); i++) {
        cout << Vector[i] << " ";
    }
}

void insertDataToMatrix(int vectorSize, vector <vector<TYPE> > &Matrix) {
    Matrix.resize(vectorSize);
    for (int i = 0; i < vectorSize; i++) {
        Matrix[0].push_back(1);
    }

    for (int i = 1; i < vectorSize; i++) {
        for (int j = 0; j < vectorSize; j++) {
            Matrix[i].push_back(1 / TYPE(i + j));
        }
    }
}

void printMatrix(vector <vector<TYPE> > Matrix) {
    for (int i = 0; i < Matrix.size(); i++) {
        for (int j = 0; j < Matrix[i].size(); j++) {
            cout << Matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void multiplyMatrixByVector(int matrixSize, vector <vector<TYPE> > &Matrix, vector<TYPE> &Vector,
                            vector<TYPE> &Output) {
    Output.resize(matrixSize);
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixSize; j++) {
            Output[i] += (Matrix[i][j] * Vector[j]);
        }
    }
}

// given A Matrix and B vector returns matrix AB
vector <vector<TYPE> > createExtendedMatrix(int matrixSize, vector <vector<TYPE> > Matrix, vector<TYPE> Vector) {
    vector <vector<TYPE> > ExtendedMatrix;
    ExtendedMatrix = Matrix;
    for (int i = 0; i < matrixSize; i++) {
        ExtendedMatrix[i].push_back(Vector[i]);
    }
    return ExtendedMatrix;
}

// Matrix stands for A, Vector stands for B => Matrix A is (A|B) - extended matrix
vector<TYPE> gaussianElimination(int matrixSize, vector<vector<TYPE> > Matrix, vector<TYPE> &Vector) {

    vector <vector<TYPE> > A = createExtendedMatrix(matrixSize, Matrix, Vector);
    int n = A.size();

    // elimination
    for (int i = 0; i < n; i++) {
        // Search for maximum in this column
        TYPE maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k = i + 1; k < n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = abs(A[k][i]);
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (int k = i; k < n + 1; k++) {
            TYPE tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (int k = i + 1; k < n; k++) {
            TYPE c = -A[k][i] / A[i][i];
            for (int j = i; j < n + 1; j++) {
                if (i == j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }

    // Solve equation Ax=b for an upper triangular matrix A
    vector<TYPE> x(n);
    for (int i = n - 1; i >= 0; i--) {
        x[i] = A[i][n] / A[i][i];
        for (int k = i - 1; k >= 0; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}

double calculateVectorNorm(vector<TYPE> Vector) {
    double sum = 0;
    for(int i=0; i<Vector.size(); i++) {
        sum += Vector[i] * Vector[i];
    }
    return sqrt(sum);
}
