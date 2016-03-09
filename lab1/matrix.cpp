#include "matrix.hpp"
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>

void generateRandomVector(unsigned vectorSize, vector<TYPE> &Vector) {
    srand(time(NULL));
    for (unsigned i = 0; i < vectorSize; i++) {
        int randomNumber = rand() % 2;
        if (randomNumber == 0) randomNumber = -1;
        Vector.push_back(randomNumber);
    }
}

void printVector(vector<TYPE> Vector) {
    for (unsigned i = 0; i < Vector.size(); i++) {
        cout << Vector[i] << " " << endl;
    }
}

void insertDataToMatrix(unsigned vectorSize, vector<vector<TYPE> > &Matrix) {
    Matrix.resize(vectorSize);
    for (unsigned i = 0; i < vectorSize; i++) {
        Matrix[0].push_back(1);
    }

    for (unsigned i = 1; i < vectorSize; i++) {
        for (unsigned j = 0; j < vectorSize; j++) {
            Matrix[i].push_back(1 / TYPE(i + j));
        }
    }
}

void printMatrix(vector <vector<TYPE> > Matrix) {
    for (unsigned i = 0; i < Matrix.size(); i++) {
        for (unsigned j = 0; j < Matrix[i].size(); j++) {
            cout << Matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void multiplyMatrixByVector(unsigned matrixSize, vector<vector<TYPE> >&Matrix, vector<TYPE> &Vector, vector<TYPE> &Output) {
    Output.resize(matrixSize);
    for(unsigned i=0; i<matrixSize; i++) {
        for(unsigned j=0; j<matrixSize; j++) {
            Output[i] += (Matrix[i][j]*Vector[j]);
        }
    }
}