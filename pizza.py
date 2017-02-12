#!/usr/bin/python3

import sys

if not len(sys.argv) == 2:
	print("Usage: pizza [file]")
	sys.exit(-1)

fo = open(sys.argv[1], "r")
(R,C,H,L) = fo.readline()[:-1].split(" ")
pizza = []
for line in fo:
	pizza.append(line[:-1])
fo.close()

