#!/bin/bash
for i in {1..2}; do
	echo Running test \#$i
	cat testes3/$i.in | python3 heuristicas.py
done