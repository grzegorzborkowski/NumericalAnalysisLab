#!/usr/bin/env bash
for i in {1..29}
do
    ./main 3 ${i}> tests_zad3/gauss/test+${i}+double.out
done
