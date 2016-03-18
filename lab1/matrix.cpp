#include "matrix.hpp"

void generateRandomVector(int vectorSize, vector<TYPE> &Vector) {
    srand(time(NULL));
    for (int i = 0; i < vectorSize; i++) {
        int randomNumber = rand() % 2;
        if (randomNumber == 0) randomNumber = -1;
        Vector.push_back(randomNumber);
    }
}

void printVector(vector<TYPE> Vector) {
    for (unsigned i = 0; i < Vector.size(); i++) {
        cout << Vector[i] << " ";
    }
}

void printSizeOfVector(vector<TYPE> Vector) {
    cout << Vector.size() << endl;
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

void insertDataToMatrixZad2(int vectorSize, vector<vector<TYPE> > &Matrix) {
    Matrix.resize(vectorSize);
    for(int i=0; i<vectorSize; i++) {
        Matrix[i].resize(vectorSize);
    }

    for(int i=0; i<vectorSize; i++) {
        for(int j=0; j<vectorSize; j++) {
            if(j>=i) Matrix[i][j] = TYPE(2*(i+1))/TYPE(j+1);
            if(j<i) Matrix[i][j] = Matrix[j][i];
        }
    }
}
/*

Zadanie 3: b) k=6, m=1
*/
void insertDataToMatrixZad3(int vectorSize, vector<vector<TYPE> > &Matrix) {
    Matrix.resize(vectorSize);
    for(int i=0; i<vectorSize; i++) {
        Matrix[i].resize(vectorSize);
    }

    for(int i=0; i<vectorSize; i++) {
        for(int j=0; j<vectorSize; j++) {
            if(i==i) Matrix[i][i] = -i - 6;
            if(j==i+1) Matrix[i][j] = i;
            if(j==i-1) Matrix[i][j] = 1 / TYPE(i+1);
            if(i-1>j && j>i+1) Matrix[i][j] = 0;
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

void calculateNormOfDifference(vector<TYPE> firstVector, vector<TYPE> secondVector) {
    double sum = 0;
    for(unsigned i=0; i<firstVector.size(); i++) {
        double tmp =  firstVector[i] - secondVector[i];
        sum += tmp*tmp;
    }
    cout << sqrt(sum) << endl;
}

void tridiagonalThomas(int vectorSize, vector<TYPE> A, vector<TYPE> B, vector<TYPE>C, vector<TYPE>&Soltuion, vector<TYPE>D) {
    vector<TYPE> C1;
    C1.resize(vectorSize);
    C1.push_back(C[0] / B[0]);
    for(int i=1; i<vectorSize; i++) {
        C1.push_back(C[i]/(B[i]-A[i]*C1[i-1]));
    }
    vector<TYPE> D1;
    D1.resize(vectorSize);
    D1.push_back(D[0]/B[0]);
    for(int i=1; i<vectorSize; i++) {
        D1.push_back((D[i] - A[i]*D1[i-1])/(B[i]-A[i]*C1[i]));
    }

}