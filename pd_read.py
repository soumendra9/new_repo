#!/usr/bin/python3
import pandas as pd
import sys

given_file = sys.argv[1]

df = pd.read_csv(given_file)

print (df.tail(-1))

columns = df.columns
for col in columns:
    print(col)

columns = df["b"]
print (columns)
