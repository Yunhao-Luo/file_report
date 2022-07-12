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

import pandas as pd
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
plt.show()