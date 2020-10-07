import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
fname = 'filtered_140_medium_unscaled.csv'
new_val= "120."
FH=open(fname)
line1=FH.readline()
line2=FH.readline()
FH.close()

num1 = line1.split(',')
fnum1 = np.array(num1).astype(float)

num2 = line2.split(',')
fnum2 = np.array(num2).astype(float)

new_num1 = new_val.split(',')
fnew_num1 = np.array(new_num1).astype(float)


x = fnum1
y = fnum2

new_x =  fnew_num1


B1 = sum((x - np.mean(x)) * (y - np.mean(y))) / sum( (x - np.mean(x))**2 )
B0 = np.mean(y) - B1 * np.mean(x)
z = B0 + B1 * x
new_z = B0 + B1*new_x

print(new_z)
plt.scatter(x,y)
plt.plot(x, z)
plt.show()
