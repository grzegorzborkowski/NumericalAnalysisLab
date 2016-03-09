#ifndef _MATRIX_H
#define _MATRIX_H_

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>

using namespace std;

void generateRandomVector(unsigned vectorSize, vector<double> &Vector);
void printVector(vector<double> Vector);
void insertDataToMatrix(unsigned vectorSize, vector <vector<double> > &Matrix);
void printMatrix(vector <vector<double> > Matrix);
void multiplyMatrixByVector(unsigned matrixSize, vector <vector<double> > &Matrix, vector<double> &Vector,
                            vector<double> &Output);

#endif