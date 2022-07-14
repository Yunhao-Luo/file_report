""" import matplotlib.pyplot as plt
   
Product = ['Computer','Monitor','Laptop','Printer','Tablet']
Quantity = [320,450,300,120,280]

ax = plt.barh(Product,Quantity)
plt.title('Store Inventory')
plt.ylabel('Product')
plt.xlabel('Quantity')



plt.show()
 """

""" 
import numpy as np
import matplotlib.pyplot as plt

#create data for two teams
quarter = ['Q1', 'Q2', 'Q3', 'Q4']
product_A = [14, 17, 12, 9]
product_B = [7, 15, 24, 18]

#define chart parameters
N = 4 
barWidth = 0.5
xloc = np.arange(N)

#create stacked bar chart
p1 = plt.barh(xloc, product_A, height=barWidth, color='springgreen')
p2 = plt.barh(xloc, product_B, height=barWidth, color='coral')

#add labels, title, tick marks, and legend
plt.title('Sales by Product & Quarter')

#display chart
plt.show() """

""" import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

continent = ["Africa","Americas","Asia","Europe","Oceania"]
lifeExp=[49,65,60,72,74]
df = pd.DataFrame({"continent":continent, "lifeExp":lifeExp})

plt.figure(figsize=(8, 6))
splot=sns.barplot(x="continent",y="lifeExp",data=df)
plt.xlabel("Continent", size=16)
plt.ylabel("LifeExp", size=16)
plt.bar_label(splot.containers[0],size=16,label_type='center')
plt.show() """

""" import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

dates = [0.1, 0.2, 0.53, 0.54, 0.75, 0.96, 1.1, 3.2, 3.53, 3.54, 4.75, 9.96]
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

dates = [3,4,6,8,8.5,9,11,12,13,0,0,0]
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

plt.show() """

""" 
import numpy as np
import matplotlib.pyplot as plt

#define data
x = np.array([8, 13, 14, 15, 15, 20, 25, 30, 38, 40])
y = np.array([5, 4, 18, 14, 20, 24, 28, 33, 30, 37])

#create scatterplot
plt.scatter(x, y)

#calculate equation for quadratic trendline
z = np.polyfit(x, y, 2)
p = np.poly1d(z)
line = [5]*10
#add trendline to plot
plt.plot(x, line)
plt.show() """

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


Data1 = {'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2],
        'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
       }   
df1 = DataFrame(Data1,columns=['Unemployment_Rate','Stock_Index_Price'])


Data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
        'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
       }   
df2 = DataFrame(Data2,columns=['Year','Unemployment_Rate'])


with PdfPages(r'C:\Users\WorldViz.VIZBOX-03\Desktop\Charts.pdf') as export_pdf:
  
    plt.scatter(df1['Unemployment_Rate'], df1['Stock_Index_Price'], color='green')
    plt.title('Unemployment Rate Vs Stock Index Price', fontsize=10)
    plt.xlabel('Unemployment Rate', fontsize=8)
    plt.ylabel('Stock Index Price', fontsize=8)
    plt.grid(True)
    export_pdf.savefig()
    plt.close()
      
    plt.plot(df2['Year'], df2['Unemployment_Rate'], color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=10)
    plt.xlabel('Year', fontsize=8)
    plt.ylabel('Unemployment Rate', fontsize=8)
    plt.grid(True)
    export_pdf.savefig()
    plt.close()