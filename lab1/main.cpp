#include "matrix.hpp"

void generate_zad1_tests() {
    int matrixSizes[20] = {1,2,4,6,8,10,12,14,16,18,20,25,30,40,50,75,100,120,150,200};
    int i=17;
        string fileName = "tests_zad1/test" + to_string(i) + "double.out";
        cout << fileName << endl;
        int matrixSize = matrixSizes[i];
        vector<vector<TYPE> > Matrix;
        Matrix.resize(matrixSize);
        vector<TYPE> X;
        generateRandomVector(matrixSize, X);
        cout << "Wygenerowany wektor X: ";
        printVector(X);
        cout << endl;
        cout << "Rozmiar wektora X: ";
        printSizeOfVector(X);

        insertDataToMatrix(matrixSize, Matrix);
        cout << "Macierz : ";
        printMatrix(Matrix);


        vector<TYPE> Vector;
        multiplyMatrixByVector(matrixSize, Matrix, X, Vector);
        vector<TYPE> solution = gaussianElimination(matrixSize, Matrix, Vector);
        cout << "Rozwiazanie ";
        printVector(solution);
        cout << endl;

        cout << "Roznica norm ";
        calculateNormOfDifference(X, solution);
}



int main() {
    generate_zad1_tests();
    return 0;
}
