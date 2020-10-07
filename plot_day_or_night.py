#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os import path
import datetime
from matplotlib.dates import date2num, MINUTES_PER_DAY, SEC_PER_DAY
from matplotlib.dates import DateFormatter
from datetime import datetime, timedelta


subjectid = "32"#input("Subject ID: ")
fname1 = "2018-12-15"#input("Date: ")
day_or_night = "day" #input("day or night: ")
#read and clean a file
def rcf(type,fname, day_or_night):
    filepath1 = "/home/agmfamily/Tutorial/"+subjectid+"/"+fname+"_"+type+"_"+day_or_night+".csv"
    if path.exists(filepath1):
        df = pd.read_csv(filepath1)
        df.drop_duplicates(inplace = True)
        df.dropna(inplace = True)
    else:
        print(fname, " does not exist")
        exit()
    return df
titles = [fname1+" BVP", fname1+" EDA", fname1+" TEMP"]
fig, ax1 = plt.subplots(2, sharex = True) #Srishti_TODO: change to 3 later
i = 0
for item in ['BVP', 'EDA']: #Srishti_TODO: Add back EDA, BVP and # tmp later
    #, 'EDA',
    df = rcf(item, fname1, day_or_night)
    fnum2 = np.array(df.iloc[:,1]).astype(float)
    fnum1 = np.array(df["UTCTimeStamp"]).astype(float)
    if fnum1[-1]-fnum1[0]>1: #SRISHTI_TODO: change to 3600 later
        time = []
        data = []
        #converting UTC time into HH/MM/SS
        for idx in range(len(fnum1)):
            d = datetime.utcfromtimestamp(fnum1[idx])
            if day_or_night == "day":
                if d.hour<20 and d.hour>=8:
                    time.append(d)
                    data.append(fnum2[idx])
            elif day_or_night == "night":
                if d.hour>=20 and d.hour<8:
                    time.append(d)
                    data.append(fnum2[idx])
        ax1[i].plot(time, data)
        plt.xlabel("Time")
        ax1[i].set_title(titles[i]+"_"+day_or_night)
        ax1[i].xaxis.set_major_formatter(DateFormatter('%d:%H:%M:%S'))
        plt.setp(ax1[i].get_xticklabels(), rotation=30, ha="right")
    else:
        print ("ERROR: more data expected for ", item)

    i = i+1
    print(i)
    break
plt.suptitle("Subject "+ subjectid)
plt.show()
