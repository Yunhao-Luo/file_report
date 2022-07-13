import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

dates = [22, 26, 31, 35, 39, 43, 47, 51, 61, 65, 70, 79, 83, 88, 96, 101, 106, 110, 115, 119, 124, 132, 136, 140, 150, 155, 160, 171, 176, 182, 186, 190, 204, 209, 213, 217, 225, 229, 232, 235, 238, 248, 253, 257]
names = ['a', 'b', 'c', 'd', 'e', 'f']

# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(2,1)#(figsize=(8.8, 4), constrained_layout=True)

ax[0].vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax[0].plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax[0].annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")

# remove y axis and spines
ax[0].yaxis.set_visible(False)
ax[0].xaxis.set_visible(False)
ax[0].spines[["left", "top", "right"]].set_visible(False)

ax[0].margins(y=0.1)

dates = [22, 26, 31, 35, 39, 43, 47, 51, 61, 65, 70, 79, 83, 88, 96, 101, 106, 110, 115, 119, 124, 132, 136, 140, 150, 155, 160, 171, 176, 182, 186, 190, 204, 209, 213, 217, 225, 229, 232, 235, 238, 248, 253, 257]
names = ['a', 'b', 'c', 'd', 'e', 'f']

ax[1].vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax[1].plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax[1].annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")

# remove y axis and spines
ax[1].yaxis.set_visible(False)
ax[1].xaxis.set_visible(False)
ax[1].spines[["left", "top", "right"]].set_visible(False)

ax[1].margins(y=0.1)

plt.show()