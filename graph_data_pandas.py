#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

fname =input("What date would you like to see? ")
BVP = pd.read_csv("/home/agmfamily/Tutorial/Data_6-13/2018-08-25_BVP1.csv", header=0, index_col=0, parse_dates=True)
print ("reading BVP")
EDA = pd.read_csv("/home/agmfamily/Tutorial/Data_6-13/2018-08-25_EDA1.csv", header=0, index_col=0, parse_dates=True)
print ("reading EDA")
TEMP = pd.read_csv("/home/agmfamily/Tutorial/Data_6-13/2018-08-25_TEMP1.csv", header=0, index_col=0, parse_dates=True)
print ("reading  TEMP")
photo = BVP['PhotoplethysmographReading']
micro = EDA['Microsiemens']
cel = TEMP['Temperature(Celsius)']
frame = {"BVP":photo, "EDA":micro, "TEMP":cel}
df = pd.DataFrame(frame)
df.plot(subplots = True)
plt.show()


1.535069e+09    -1.11
1.535151e+09   -20.40
