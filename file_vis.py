#!/usr/bin/python3
import pandas as pd
import sys

file = input("welcome to my file analyzer! What file would you like to see? ")
print (" ")
print ("reading", file, "...")
print (" ")

df = pd.read_csv(file)
columns = df.columns
print(file, " has ", len(df), " rows and ", len(columns), " columns.")
print("These are the columns: ", ", ".join(columns))

column_name = input("which column do you want to report? ")
report_col = df[column_name]
print (report_col)

print("There is/are ", report_col.isnull().sum(), " missing values in this column.")
print(df[column_name])

for col_name in columns:
    col=df[col_name]
    if col.isnull().sum():
        print  (col.name, " has null value(s)")
