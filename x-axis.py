#!/usr/bin/python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
from matplotlib.dates import date2num, MINUTES_PER_DAY, SEC_PER_DAY
df = pd.read_csv("test.csv")
fnum2 = np.array(df["Temperature(Celsius)"]).astype(float)
fnum1 = np.array(df["UTCTimeStamp"]).astype(float)
fig, ax = plt.subplots()
x = []
for t in fnum1:
    x.append(datetime.datetime.utcfromtimestamp(t))
ax.plot(x, fnum2)
from matplotlib.dates import DateFormatter
ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
plt.show()
