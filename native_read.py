#!/usr/bin/python3
import sys

print(sys.argv[1])
given_file=sys.argv[1]

FH = open(given_file)
lines = FH.readlines()

print(lines)

FH.close()
