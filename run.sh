#!/bin/bash
for i in {1..10}; do
	echo Running test \#$i
	time cat testes/$i.in | python3 v2astar.py
done