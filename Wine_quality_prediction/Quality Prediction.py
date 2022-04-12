# import pandas
import pandas as pd

# import numpy
import numpy as np

# import seaborn
import seaborn as sb

# import matplotlib

import matplotlib.pyplot as plt

# creating Dataframe object
df = pd.read_csv('winequalityN.csv')
print(df.head())
print(df.info())
print(df.describe())

df.hist(bins=25,figsize=(10,10))
# display histogram
plt.show()

plt.figure(figsize=[10,6])
# plot bar graph
plt.bar(df['quality'],df['alcohol'],color='red')
# label x-axis
plt.xlabel('quality')
#label y-axis
plt.ylabel('alcohol')

# ploting heatmap
plt.figure(figsize=[19,10],facecolor='blue')
sb.heatmap(df.corr(),annot=True)