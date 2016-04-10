#!/usr/bin/env bash
for i in {1..29}
do
    cat tests_zad3/thomas/test+${i}+float.out >> tests_zad3/thomas/float.out
    cat tests_zad3/thomas/test+${i}+double.out >> tests_zad3/thomas/double.out
done

