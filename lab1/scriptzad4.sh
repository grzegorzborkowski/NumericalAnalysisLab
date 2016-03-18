#!/usr/bin/env bash
for i in {1..29}
do
    ./main 4 ${i}> tests_zad3/thomas/test+${i}+double.out
done
