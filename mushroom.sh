#!/usr/bin/env bash

python3 src/main.py data/mushroom_train.csv data/mushroom_test.csv
dot -Tpng trees/mytree.dot -o trees/mytree.png
feh trees/mytree.png
