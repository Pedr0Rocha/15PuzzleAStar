#!/bin/bash
for i in {1..4}; do
	echo Running test \#$i
	cat testes2/$i.in | python3 heuristicas.py
done