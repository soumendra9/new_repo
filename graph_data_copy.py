#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from os import path
import datetime
from matplotlib.dates import date2num, MINUTES_PER_DAY, SEC_PER_DAY
from matplotlib.dates import DateFormatter

subjectid = input("what is the subject id? ")
fname = input("What date would you like to see? ")
#read and clean a file
def rcf(type,fname):
    filepath = "/home/agmfamily/Tutorial/"+subjectid+"/"+fname+"_"+type+".csv"
    if path.exists(filepath):
        df = pd.read_csv(filepath)
        df.drop_duplicates(inplace = True)
        df.dropna(inplace = True)
    else:
        print("file does not exist")
        exit()
    return df
titles = [fname+" BVP", fname+" BVP", fname+" EDA", fname+" EDA", fname+" TEMP", fname+" TEMP" ]
fig, ax = plt.subplots(3, sharex = True)
i = 0
for item in ['BVP', 'EDA', 'TEMP']:
    df = rcf(item, fname)
    fnum2 = np.array(df.iloc[:,1]).astype(float)
    fnum1 = np.array(df["UTCTimeStamp"]).astype(float)
    if fnum1[-1]-fnum1[0]>3600:
        x_day = []
        fnum2_day = []
#converting UTC time into HH/MM/SS
        for idx in range(len(fnum1)):
            d = datetime.datetime.utcfromtimestamp(fnum1[idx])
            x_day.append(d)
            fnum2_day.append(fnum2[idx])
        ax[i].plot(x_day, fnum2_day)
        plt.xlabel("Time")
        ax[i].set_title(titles[i]+"_day")
        ax[i].xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
        plt.setp(ax[i].get_xticklabels(), rotation=30, ha="right")
        i = i+1
    else:
        print ("ERROR: more data expected for ", item)
        break
plt.show()
