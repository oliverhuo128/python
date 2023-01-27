# Copy here your program to plot sins and cosines

import matplotlib.pyplot as plt
import math

y_values =[]

for i in range(360):
    y_values.append(math.sin(i*math.pi/180.0))

plt.plot(y_values)

y_values =[]
for i in range(360):
    y_values.append(math.cos(i*math.pi/180.0))

plt.plot(y_values, 'r+')

plt.savefig('trig.png')
