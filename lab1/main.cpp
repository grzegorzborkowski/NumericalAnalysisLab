#include "matrix.hpp"

void generate_tests(int taskNumber, int i) {
        int matrixSize;
        if(taskNumber == 1) {
        int matrixSizes[20] = {1,2,4,6,8,10,12,14,16,18,20,25,30,40,50,75,100,120,150,200};
        matrixSize = matrixSizes[i];
        }
        if(taskNumber == 2 || taskNumber == 3) {
        int matrixSizes[30] = {1,2,4,6,8,10,12,14,16,18,20,25,30,40,50,75,100,120,150,200,
        300, 400, 450, 1000, 1200, 1500, 1800, 2000, 2500, 3000};
        matrixSize = matrixSizes[i];
        }
        vector<vector<TYPE> > Matrix;
        Matrix.resize(matrixSize);
        vector<TYPE> X;
        generateRandomVector(matrixSize, X);
        cout << endl;
        cout << "Rozmiar wektora X: ";
        printSizeOfVector(X);
        if(taskNumber == 1) {
        insertDataToMatrix(matrixSize, Matrix);
        }
        if(taskNumber == 2) {
        insertDataToMatrixZad2(matrixSize, Matrix);
        }
        if(taskNumber == 3) {
        insertDataToMatrixZad3(matrixSize, Matrix);
        }

        vector<TYPE> Vector;
        multiplyMatrixByVector(matrixSize, Matrix, X, Vector);
        vector<TYPE> solution = gaussianElimination(matrixSize, Matrix, Vector);

        cout << "Roznica norm ";
        calculateNormOfDifference(X, solution);
}




int main(int argc, char **argv) {
    int nr_zadania = stoi(argv[1]);
    int rozmiar_macierzy = stoi(argv[2]);
    generate_tests(nr_zadania, rozmiar_macierzy);
    return 0;
}
