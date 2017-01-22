#!/usr/bin/env bash

python3 src/main.py data/mushroom
dot -Tpng trees/mytree.dot -o trees/mytree.png
