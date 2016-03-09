#ifndef _MATRIX_H
#define _MATRIX_H_

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>

using namespace std;
#define TYPE float // this constant indicates precision of calculation

void generateRandomVector(unsigned vectorSize, vector<TYPE> &Vector);
void printVector(vector<TYPE> Vector);
void insertDataToMatrix(unsigned vectorSize, vector <vector<TYPE> > &Matrix);
void printMatrix(vector <vector<TYPE> > Matrix);
void multiplyMatrixByVector(unsigned matrixSize, vector <vector<TYPE> > &Matrix, vector<TYPE> &Vector,
                            vector<TYPE> &Output);
// Ax = B A: Matrix, x:Solution, B:Vector
void gaussianElimination(vector <vector <TYPE> > Matrix, vector<TYPE> &Solution, vector<TYPE> &Vector);

#endif