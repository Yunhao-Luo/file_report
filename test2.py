""" from datetime import datetime
import matplotlib.pyplot as plt

jobs = ['JOB1','JOB2','JOB3','JOB4']

# input wait times
waittimesin = ['03:20:50','04:45:10','06:10:40','05:30:30']
# converting wait times to float
waittimes = []
for wt in waittimesin:
    waittime = datetime.strptime(wt,'%H:%M:%S')
    waittime = waittime.hour + waittime.minute/60 + waittime.second/3600
    waittimes.append(waittime)

# input run times
runtimesin = ['00:20:50','01:00:10','00:30:40','00:10:30']
# converting run times to float    
runtimes = []
for rt in runtimesin:
    runtime = datetime.strptime(rt,'%H:%M:%S')
    runtime = runtime.hour + runtime.minute/60 + runtime.second/3600
    runtimes.append(runtime)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.barh(jobs, waittimes, align='center', height=.25, color='#00ff00',label='wait time')
ax.barh(jobs, runtimes, align='center', height=.25, left=waittimes, color='g',label='run time')
ax.set_yticks(jobs)
ax.set_xlabel('Hour')
ax.set_title('Run Time by Job')
ax.grid(True)
ax.legend()
plt.tight_layout()
#plt.savefig('C:\\Data\\stackedbar.png')
plt.show() """

""" 

import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [0.2,0.3,0.1,0.05,0.1]
women_means = [25, 32, 34, 20, 25]
men_std = [0.5,0.5,0.5,0.5,0.5]
women_std = [0.5,0.5,0.5,0.5,0.5]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(2,1)
levels = np.tile([1,1,1,1,1,1],
                 int(np.ceil(len(men_means)/6)))[:len(men_means)]

ax[0].vlines(men_means, 0, levels, color="tab:red")  # The vertical stems.
ax[0].plot(men_means, np.zeros_like(men_means), "-o",
                    color="k", markerfacecolor="w")  # Baseline and markers on it.
ax[1].barh(labels, men_means, width, yerr=men_std)
ax[1].barh(labels, women_means, width, yerr=women_std)

ax[0].xaxis.set_visible(False)
ax[1].xaxis.set_visible(False)

plt.show() """

""" print(3%2)

# importing package
from tkinter import Y
from turtle import width
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(3,1)
# create data
x = ['A']
y1 = 2 #np.array([10, 20, 10, 30])
y2 = 4 #np.array([20, 25, 15, 25])
y3 = 1 #np.array([12, 15, 19, 6])
y4 = 7 #np.array([10, 29, 13, 19])

# plot bars in stack manner
ax[0].barh(x, y1, color='r')
ax[0].barh(x, y2, left=y1, color='b')
ax[0].barh(x, y3, left=y1+y2, color='r')
ax[0].barh(x, y4, left=y1+y2+y3, color='b') """

""" ax[1].barh(x, y1, color='r')
ax[1].barh(x, y2, left=y1, color='b')
ax[1].barh(x, y3, left=y1+y2, color='r')
ax[1].barh(x, y4, left=y1+y2+y3, color='b')
ax[1].yaxis.set_visible(False)
ax[1].xaxis.set_visible(False)
ax[1].spines[["left", "right"]].set_visible(False)
ax[1].plot(X=20) """

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages(r'C:\Users\WorldViz.VIZBOX-03\Desktop\Charts.pdf') as export_pdf:
    fig, ax = plt.subplots(5,1)
    for i in range(0, 5):
        data = [23, 23, 32, 24, 12]
        ax[i].barh(["1a","1b","1c","2d","3d"], data)
        y_line = [30]*5
        x_line = [0]*5
        ax[i].plot(y_line, ["1a","1b","1c","2d","3d"], color="r")
        ax[i].set_title('testing')
        ax[i].xaxis.set_visible(False)
        ax[i].spines[["left", "top", "right", "bottom"]].set_visible(False)

        data = [23, 50, 32, 12, 12]
        ax[i].barh(["1a","1b","1c","2d","3d"], data)
        y_line = [30]*5
        x_line = [0]*5
        ax[i].plot(y_line, ["1a","1b","1c","2d","3d"], color="r")
        ax[i].set_title('testing')
        ax[i].xaxis.set_visible(False)
        ax[i].spines[["left", "top", "right", "bottom"]].set_visible(False)
    
    export_pdf.savefig()

    fig, ax = plt.subplots(5,1)
    for i in range(0, 5):
        data = [23, 23, 32, 24, 12]
        ax[i].barh(["1a","1b","1c","2d","3d"], data)
        y_line = [30]*5
        x_line = [0]*5
        ax[i].plot(y_line, ["1a","1b","1c","2d","3d"], color="r")
        ax[i].set_title('testing')
        ax[i].xaxis.set_visible(False)
        ax[i].spines[["left", "top", "right", "bottom"]].set_visible(False)

        data = [23, 50, 32, 12, 12]
        ax[i].barh(["1a","1b","1c","2d","3d"], data)
        y_line = [30]*5
        x_line = [0]*5
        ax[i].plot(y_line, ["1a","1b","1c","2d","3d"], color="r")
        ax[i].set_title('testing')
        ax[i].xaxis.set_visible(False)
        ax[i].spines[["left", "top", "right", "bottom"]].set_visible(False)
    
    export_pdf.savefig()
    plt.close()