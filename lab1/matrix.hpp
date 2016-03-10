#ifndef _MATRIX_H
#define _MATRIX_H_

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <math.h>
#include <vector>
#include <cmath>

using namespace std;
#define TYPE float // this constant indicates precision of calculation
const double eps = 1e-12;

void generateRandomVector(int vectorSize, vector<TYPE> &Vector);
void printVector(vector<TYPE> Vector);
void insertDataToMatrix(int vectorSize, vector <vector<TYPE> > &Matrix);
void printMatrix(vector <vector<TYPE> > Matrix);
void multiplyMatrixByVector(int matrixSize, vector <vector<TYPE> > &Matrix, vector<TYPE> &Vector,
                            vector<TYPE> &Output);
// Ax = B A: Matrix, x:Solution, B:Vector
vector<TYPE> gaussianElimination(int matrixSize, vector<vector <TYPE> > A, vector<TYPE> &Vector);
double calculateVectorNorm(vector<TYPE> Vector);
#endif