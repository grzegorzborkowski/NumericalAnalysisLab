#!/usr/bin/env bash
for i in {1..29}
do
    ./main 4 ${i}> tests_POPRAWIONE/thomas/test+${i}+double.out
done
