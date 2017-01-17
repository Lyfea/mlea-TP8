#!/usr/bin/env bash

python3 src/main.py data/mushroom
pdflatex -output-directory=trees trees/mytree.tex
