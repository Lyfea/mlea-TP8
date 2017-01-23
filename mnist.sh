#!/usr/bin/env bash

python3 src/main.py data/mnist_train.csv data/mnist_test.csv
dot -Tsvg trees/mytree.dot -o trees/mytree.svg
