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

for a in range(len(df.corr().columns)):
    for b in range(a):
        if abs(df.corr().iloc[a,b]) >0.7:
            name = df.corr().columns[a]
            print(name)


new_df=df.drop('total sulfur dioxide',axis=1)


new_df.isnull().sum()


new_df.update(new_df.fillna(new_df.mean()))


# catogerical vars
next_df = pd.get_dummies(new_df,drop_first=True)
# display new dataframe
next_df

#
# df_dummies[''best quality''] = [ 1 if x>=7 else 0 for x in df.quality]
# print(df_dummies)

plt.figure(figsize=[10,6])
# plot bar graph
plt.bar(df['quality'],df['alcohol'],color='red')
# label x-axis
plt.xlabel('quality')
#label y-axis
plt.ylabel('alcohol')

