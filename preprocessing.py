# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:42:26 2024

@author: Admin
"""

import pandas as pd
coal_ore=pd.read_csv("COALINDIA (20240408000000000 _ 20190408000000000).csv")
coal_ore.count()
coal_ore.columns
coal_ore.describe()
coal_ore.info()


# typecasting:
import pandas as pd

# Remove the additional characters from the date string
coal_ore['Date'] = coal_ore['Date'].str.replace(r'\s+\(.*\)', '', regex=True)

# Convert the 'Date' column to datetime format using the specified format
coal_ore['Date'] = pd.to_datetime(coal_ore['Date'], format='%a %b %d %Y %H:%M:%S GMT%z')

coal_ore['Date']=coal_ore["Date"].dt.strftime("%d-%m-%Y")


# duplicate handling:
coal_ore.duplicated()
coal_ore.duplicated().sum()
# Out[44]: 0

# missing value
coal_ore.isna()
coal_ore.isna().sum()
# Out[46]: 
# Date                      0
# Open                      0
# High                      0
# Low                       0
# Close                     0
# Trend Supertrend (7,3)    0
# MACD  (12,26,9)           0
# Signal MACD (12,26,9)     0
# MACD (12,26,9)_hist       0
# Volume                    0
# dtype: int64


# outliers:
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(coal_ore["Open"],color="green")
plt.title("boxplot of open")

plt.subplot(2,3,2)
sns.boxplot(coal_ore["High"],color="green")
plt.title("boxplot of open")

plt.subplot(2,3,3)
sns.boxplot(coal_ore["Low"],color="green")
plt.title("boxplot of Low")

plt.subplot(2,3,4)
sns.boxplot(coal_ore["Close"],color="green")
plt.title("boxplot of Close")

plt.subplot(2,3,5)
sns.boxplot(coal_ore["Trend Supertrend (7,3)"],color="green")
plt.title("boxplot of Trend Supertrend (7,3)")


plt.show()

plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(coal_ore["MACD (12,26,9)"],color="green")
plt.title("boxplot of MACD (12,26,9)")


plt.subplot(2,3,2)
sns.boxplot(coal_ore["Signal MACD (12,26,9)"],color="green")
plt.title("boxplot of Signal MACD (12,26,9)")

plt.subplot(2,3,3)
sns.boxplot(coal_ore["MACD (12,26,9)_hist"],color="green")
plt.title("boxplot of MACD (12,26,9)_hist")

plt.subplot(2,3,4)
sns.boxplot(coal_ore["Volume"],color="green")
plt.title("boxplot of Volume")

plt.show()

# all the column contain outliers

from feature_engine.outliers import Winsorizer

# Create a Winsorizer instance
iqr_winsorizer = Winsorizer(capping_method="iqr", 
                            fold=1.5, tail="both", 
                            variables=['Open','High', 'Low', 'Close',
                                       'Trend Supertrend (7,3)', 'MACD (12,26,9)', 
                                       'Signal MACD (12,26,9)', 
                                       'MACD (12,26,9)_hist', 'Volume'])

# Fit and transform the data using the Winsorizer for each column
coal_ore[['Open','High', 'Low', 'Close', 
          'Trend Supertrend (7,3)', 
          'MACD (12,26,9)', 
          'Signal MACD (12,26,9)', 
          'MACD (12,26,9)_hist', 'Volume']] = iqr_winsorizer.fit_transform(coal_ore[['Open','High', 'Low', 
                                                                                     'Close', 'Trend Supertrend (7,3)',
                                                                                     'MACD (12,26,9)', 'Signal MACD (12,26,9)', 
                                                                                     'MACD (12,26,9)_hist', 'Volume']])


# zero variance
numeric_columns = coal_ore.select_dtypes(include=['number']).columns
variance = coal_ore[numeric_columns].var()
print(variance)

# output:
#     Open                      4.021828e+03
#     High                      4.283580e+03
#     Low                       4.145745e+03
#     Close                     4.212956e+03
#     Trend Supertrend (7,3)    3.594466e+03
#     MACD  (12,26,9)           1.258180e+02
#     Signal MACD (12,26,9)     1.155633e+02
#     MACD (12,26,9)_hist       8.329026e+00
#     Volume                    7.679954e+14
#     dtype: float64

coal_ore.to_csv('COALINDIA.csv', index=False)

# -------------------------------------------------------------------------------------------------------------
#mean
print("Mean Open:", coal_ore['Open'].mean())
print("Mean High:", coal_ore['High'].mean())
print("Mean Low:", coal_ore['Low'].mean())
print("Mean Close:", coal_ore['Close'].mean())
print("Mean Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].mean())
print("Mean MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].mean())
print("Mean Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].mean())
print("Mean MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].mean())
print("Mean Volume:", coal_ore['Volume'].mean())

# output:
# Mean Open: 185.42566316793892
# Mean High: 193.57744274809164
# Mean Low: 178.95282442748092
# Mean Close: 186.27328721374042
# Mean Trend Supertrend (7,3): 175.74745229007635
# Mean MACD  (12,26,9): 2.2651622137404575
# Mean Signal MACD (12,26,9): 1.8045419847328243
# Mean MACD (12,26,9)_hist: 0.8110973282442748
# Mean Volume: 55730747.44942748

# Median
print("Median Open:", coal_ore['Open'].median())
print("Median High:", coal_ore['High'].median())
print("Median Low:", coal_ore['Low'].median())
print("Median Close:", coal_ore['Close'].median())
print("Median Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].median())
print("Median MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].median())
print("Median Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].median())
print("Median MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].median())
print("Median Volume:", coal_ore['Volume'].median())

# output:
# Median Open: 177.595
# Median High: 186.825
# Median Low: 169.2
# Median Close: 177.12
# Median Trend Supertrend (7,3): 181.985
# Median MACD  (12,26,9): 1.9449999999999998
# Median Signal MACD (12,26,9): 2.0549999999999997
# Median MACD (12,26,9)_hist: 0.865
# Median Volume: 50226774.5

# Variance
print("Variance Open:", coal_ore['Open'].var())
print("Variance High:", coal_ore['High'].var())
print("Variance Low:", coal_ore['Low'].var())
print("Variance Close:", coal_ore['Close'].var())
print("Variance Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].var())
print("Variance MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].var())
print("Variance Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].var())
print("Variance MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].var())
print("Variance Volume:", coal_ore['Volume'].var())
# output:
# Variance Open: 4021.827757131556
# Variance High: 4283.579704163379
# Variance Low: 4145.7453718770985
# Variance Close: 4212.9562091420485
# Variance Trend Supertrend (7,3): 3594.4660467649564
# Variance MACD  (12,26,9): 125.8180072772258
# Variance Signal MACD (12,26,9): 115.56330611125739
# Variance MACD (12,26,9)_hist: 8.329026449303184
# Variance Volume: 767995354917188.1

# Standard Deviation
print("Standard Deviation Open:", coal_ore['Open'].std())
print("Standard Deviation High:", coal_ore['High'].std())
print("Standard Deviation Low:", coal_ore['Low'].std())
print("Standard Deviation Close:", coal_ore['Close'].std())
print("Standard Deviation Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].std())
print("Standard Deviation MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].std())
print("Standard Deviation Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].std())
print("Standard Deviation MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].std())
print("Standard Deviation Volume:", coal_ore['Volume'].std())

# # output:
# Standard Deviation Open: 63.4178819981522
# Standard Deviation High: 65.4490619043801
# Standard Deviation Low: 64.38746284702557
# Standard Deviation Close: 64.90728933750083
# Standard Deviation Trend Supertrend (7,3): 59.95386598681487
# Standard Deviation MACD  (12,26,9): 11.216862630754903
# Standard Deviation Signal MACD (12,26,9): 10.750037493481472
# Standard Deviation MACD (12,26,9)_hist: 2.8860052753422307
# Standard Deviation Volume: 27712729.113481194


# range
print("Range Open:", coal_ore['Open'].max() - coal_ore['Open'].min())
print("Range High:", coal_ore['High'].max() - coal_ore['High'].min())
print("Range Low:", coal_ore['Low'].max() - coal_ore['Low'].min())
print("Range Close:", coal_ore['Close'].max() - coal_ore['Close'].min())
print("Range Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].max() - coal_ore['Trend Supertrend (7,3)'].min())
print("Range MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].max() - coal_ore['MACD  (12,26,9)'].min())
print("Range Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].max() - coal_ore['Signal MACD (12,26,9)'].min())
print("Range MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].max() - coal_ore['MACD (12,26,9)_hist'].min())
print("Range Volume:", coal_ore['Volume'].max() - coal_ore['Volume'].min())

# output:
# Range Open: 245.08375
# Range High: 248.79999999999998
# Range Low: 246.27499999999992
# Range Close: 246.53375
# Range Trend Supertrend (7,3): 234.2525
# Range MACD  (12,26,9): 45.712500000000006
# Range Signal MACD (12,26,9): 44.81999999999999
# Range MACD (12,26,9)_hist: 13.622499999999999
# Range Volume: 112794511.75

# Skewness
print("Skewness Open:", coal_ore['Open'].skew())
print("Skewness High:", coal_ore['High'].skew())
print("Skewness Low:", coal_ore['Low'].skew())
print("Skewness Close:", coal_ore['Close'].skew())
print("Skewness Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].skew())
print("Skewness MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].skew())
print("Skewness Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].skew())
print("Skewness MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].skew())
print("Skewness Volume:", coal_ore['Volume'].skew())

# output:
# Skewness Open: 1.0283249192160808
# Skewness High: 0.9805385666187735
# Skewness Low: 1.0656378813036167
# Skewness Close: 1.0102434152143318
# Skewness Trend Supertrend (7,3): 0.7208941498948935
# Skewness MACD  (12,26,9): 0.4975137327408179
# Skewness Signal MACD (12,26,9): 0.6197485326037608
# Skewness MACD (12,26,9)_hist: 0.16724704679695995
# Skewness Volume: 0.8822435489385553   
 
# Kurtosis
print("Kurtosis Open:", coal_ore['Open'].kurt())
print("Kurtosis High:", coal_ore['High'].kurt())
print("Kurtosis Low:", coal_ore['Low'].kurt())
print("Kurtosis Close:", coal_ore['Close'].kurt())
print("Kurtosis Trend Supertrend (7,3):", coal_ore['Trend Supertrend (7,3)'].kurt())
print("Kurtosis MACD  (12,26,9):", coal_ore['MACD  (12,26,9)'].kurt())
print("Kurtosis Signal MACD (12,26,9):", coal_ore['Signal MACD (12,26,9)'].kurt())
print("Kurtosis MACD (12,26,9)_hist:", coal_ore['MACD (12,26,9)_hist'].kurt())
print("Kurtosis Volume:", coal_ore['Volume'].kurt())

# output:
Kurtosis Open: 0.6533931680796456
Kurtosis High: 0.4673243397450948
Kurtosis Low: 0.6747941696590898
Kurtosis Close: 0.5134879356299988
Kurtosis Trend Supertrend (7,3): 0.0928457970530614
Kurtosis MACD  (12,26,9): 0.11094130589576778
Kurtosis Signal MACD (12,26,9): 0.3617749293418755
Kurtosis MACD (12,26,9)_hist: 0.03584299614063191
Kurtosis Volume: 0.1755699720809103

# graphical representation:
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(coal_ore["Open"],color="green")
plt.title("boxplot of open")

plt.subplot(2,3,2)
sns.boxplot(coal_ore["High"],color="green")
plt.title("boxplot of open")

plt.subplot(2,3,3)
sns.boxplot(coal_ore["Low"],color="green")
plt.title("boxplot of Low")

plt.subplot(2,3,4)
sns.boxplot(coal_ore["Close"],color="green")
plt.title("boxplot of Close")

plt.subplot(2,3,5)
sns.boxplot(coal_ore["Trend Supertrend (7,3)"],color="green")
plt.title("boxplot of Trend Supertrend (7,3)")


plt.show()

plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
sns.boxplot(coal_ore["MACD  (12,26,9)"],color="green")
plt.title("boxplot of MACD  (12,26,9)")


plt.subplot(2,3,2)
sns.boxplot(coal_ore["Signal MACD (12,26,9)"],color="green")
plt.title("boxplot of Signal MACD (12,26,9)")

plt.subplot(2,3,3)
sns.boxplot(coal_ore["MACD (12,26,9)_hist"],color="green")
plt.title("boxplot of MACD (12,26,9)_hist")

plt.subplot(2,3,4)
sns.boxplot(coal_ore["Volume"],color="green")
plt.title("boxplot of Volume")

plt.show()
  

# --------------------------------------------------------------------------------------
# scatter plot

plt.figure(figsize=(15, 10))

# Scatter plot of Open vs Close
plt.subplot(2,3,1)
plt.scatter(x=coal_ore["Open"], y=coal_ore["Close"],color="green")
plt.title("Scatter plot of Open vs Close")
plt.xlabel("Open")
plt.ylabel("Close")

# Scatter plot of High vs Low
plt.subplot(2,3,2)
plt.scatter(x=coal_ore["High"], y=coal_ore["Low"],color="green")
plt.title("Scatter plot of High vs Low")
plt.xlabel("High")
plt.ylabel("Low")

plt.show()


# ------------------------------------------------------------------------------------
plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
sns.distplot(coal_ore["Open"],color="green")
plt.xlabel("Open")
plt.ylabel("frequency")

plt.subplot(2,3,2)
sns.distplot(coal_ore["High"],color="green")
plt.xlabel("High")
plt.ylabel("frequency")

plt.subplot(2,3,3)
sns.distplot(coal_ore["Low"],color="green")
plt.xlabel("Low")
plt.ylabel("frequency")

plt.subplot(2,3,4)
sns.distplot(coal_ore["Close"],color="green")
plt.xlabel("Close")
plt.ylabel("frequency")

plt.subplot(2,3,5)
sns.distplot(coal_ore["Trend Supertrend (7,3)"],color="green")
plt.xlabel("Trend Supertrend (7,3)")
plt.ylabel("frequency")

plt.show()

# ----------------------------------------------------------------------------------
plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
sns.distplot(coal_ore["MACD (12,26,9)"],color="green")
plt.xlabel("MACD  (12,26,9)")
plt.ylabel("frequency")

plt.subplot(2,3,2)
sns.distplot(coal_ore["Signal MACD (12,26,9)"],color="green")
plt.xlabel("Signal MACD (12,26,9)")
plt.ylabel("frequency")

plt.subplot(2,3,3)
sns.distplot(coal_ore["MACD (12,26,9)_hist"],color="green")
plt.xlabel("MACD (12,26,9)_hist")
plt.ylabel("frequency")

plt.subplot(2,3,4)
sns.distplot(coal_ore["Volume"],color="green")
plt.xlabel("Volume")
plt.ylabel("frequency")

plt.show()






