#!/usr/bin/python3
import pandas as pd
import sys
from os import path

print ("welcome to my file analyzer! Here are the things you can do:")
def get_help():
    print("\t1. read <filename>")#done
    print("\t2. get_col_names")#done
    print("\t3. is_columm_null <col_name>")#done
    print("\t4. is_row_null <row_index>")#done
    print("\t5. show_column <column_name>")#done
    print("\t6. show_row <row_index")#done
    print("\t7. summary_file>")#done
    print("\t8. help")#done
    print("\t9. exit")#done

print(get_help())
 
def get_col_names(df):
    columns = df.columns
    print("These are the columns: ", ", ".join(columns))

file_read = False
while True:
    choice = input("what would you like to do? ")
    tokens=choice.split(" ")
#read a csv file
    if tokens[0] == "read" or tokens[0] == "1":
        if len(tokens) != 2:
            print("ERROR: file name expected")
            continue
        print("reading the file ", tokens[1], "...")
        if path.exists(tokens[1]):
            df=pd.read_csv(tokens[1])
            file_read = True
            file_name = tokens[1]
        else:
            print ("ERROR file does not exist; read another file")

#get column names
    elif tokens[0] == "get_col_names" or tokens[0] == "2":
        if file_read == True:
            print (get_col_names(df))
        else:
            print("info: no flie read yet")

#is the column null
    elif tokens[0] == "is_columm_null" or tokens[0] == "3":
        if len(tokens) != 2:
            print("ERROR: column name expected")
            continue
        if file_read == True:
            if tokens[1] in df:
                col_name = tokens[1]
                col = df[col_name]
                if col.isnull().sum():
                    print  (col.name, " has null value(s)")
                else:
                    print(col_name, " has no null value(s)")
            else:
                print("ERROR:", tokens[1], " is not a valid column")
        else:
            print ("info: no file read yet")

#is the row null
    elif tokens[0] == "is_row_null" or tokens[0] == "4":
        if len(tokens) != 2:
            print("ERROR: row index expected")
            continue
        if file_read == True:
            row = df.loc[[row_num],:]
            if row.isnull().any().sum():
                print ("Row ", row_num, " has null value(s)")
            else:
                print ("Row ", row_num, " has no null value(s)")
        else:
            print("info: no file read yet")

#print a column in a file
    elif tokens[0] == "show_column" or tokens[0] == "5":
        if len(tokens) != 2:
            print("ERROR: column name expected")
            continue
        if file_read == True:
            if tokens[1] in df:
                report_col = df[tokens[1]]
                print (report_col)
            else:
                print("ERROR:", tokens[1], " is not a valid column")
        else:
            print ("info: no file read yet")
            continue

#show a row in a file
    elif tokens[0] == "show_row" or tokens[0] == "6":
        if len(tokens) != 2:
            print("ERROR: row index expected")
            continue
        if file_read == True:
            row_num = int(tokens[1])
            row = df.loc[[row_num],:]
            print (row)
        else:
            print ("info: no file read yet")

#display file
    elif tokens[0] == "summary_file" or tokens[0] == "7":
        if file_read == True:
            num_rows = len(df)
            num_col = len(df.columns)
            print(file_name, " has ", num_rows, " rows and ", num_col, " columns.")
        else:
            print ("info: no file read yet")

#help menu
    elif tokens[0]=="help" or tokens[0]=="8":
        print(get_help())

#exit the program
    elif tokens[0]=="exit" or tokens[0]=="9":
        exit()
    else:
        print ("Invalid Command")
