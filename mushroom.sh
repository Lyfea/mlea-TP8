#!/usr/bin/env bash

python3 src/main.py data/mushroom.csv
dot -Tpng trees/mytree.dot -o trees/mytree.png
feh trees/mytree.png
