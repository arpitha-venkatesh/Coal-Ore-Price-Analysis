# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:19:01 2024

@author: Admin
"""

import pandas as pd
coal_ore=pd.read_csv("COALINDIA (20240408000000000 _ 20190408000000000).csv")
coal_ore.count()
coal_ore.columns
coal_ore.describe()
coal_ore.info()


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
# Mean Open: 189.51339694656488
# Mean High: 199.05706106870232
# Mean Low: 182.76919847328244
# Mean Close: 191.22416030534353
# Mean Trend Supertrend (7,3): 176.04572519083968
# Mean MACD  (12,26,9): 3.2988167938931294
# Mean Signal MACD (12,26,9): 2.485038167938932
# Mean MACD (12,26,9)_hist: 0.8133969465648855
# Mean Volume: 57622231.5648855

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
Median Open: 177.595
Median High: 186.825
Median Low: 169.2
Median Close: 177.12
Median Trend Supertrend (7,3): 181.985
Median MACD  (12,26,9): 1.9449999999999998
Median Signal MACD (12,26,9): 2.0549999999999997
Median MACD (12,26,9)_hist: 0.865
Median Volume: 50226774.5

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
    # Variance Open: 5659.211678454856
    # Variance High: 6529.709807038402
    # Variance Low: 5659.415833454709
    # Variance Close: 6200.583372280717
    # Variance Trend Supertrend (7,3): 3691.172436828408
    # Variance MACD  (12,26,9): 192.88885185136436
    # Variance Signal MACD (12,26,9): 159.86795153110472
    # Variance MACD (12,26,9)_hist: 8.361384968266504
    # Variance Volume: 1192962005534903.5

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
# Standard Deviation Open: 75.22773211027204
# Standard Deviation High: 80.80661982188342
# Standard Deviation Low: 75.22908901119771
# Standard Deviation Close: 78.74378307066989
# Standard Deviation Trend Supertrend (7,3): 60.75501984880268
# Standard Deviation MACD  (12,26,9): 13.88844310393949
# Standard Deviation Signal MACD (12,26,9): 12.643889889235224
# Standard Deviation MACD (12,26,9)_hist: 2.8916059496872157
# Standard Deviation Volume: 34539282.06455518



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
Range Open: 351.06
Range High: 384.95000000000005
Range Low: 350.25
Range Close: 365.98
Range Trend Supertrend (7,3): 253.89
Range MACD  (12,26,9): 68.07000000000001
Range Signal MACD (12,26,9): 61.93
Range MACD (12,26,9)_hist: 13.95
Range Volume: 243068229

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
# Skewness Open: 1.6587720445909897
# Skewness High: 1.7008660823266648
# Skewness Low: 1.6151334250345433
# Skewness Close: 1.6648442431211379
# Skewness Trend Supertrend (7,3): 0.7834457012203672
# Skewness MACD  (12,26,9): 1.3349772179880295
# Skewness Signal MACD (12,26,9): 1.33639981497823
# Skewness MACD (12,26,9)_hist: 0.1780584901256104
# Skewness Volume: 2.2035838076668437
    
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
Kurtosis Open: 2.9964835348709817
Kurtosis High: 3.0364628638964373
Kurtosis Low: 2.692480908358731
Kurtosis Close: 2.844631250864907
Kurtosis Trend Supertrend (7,3): 0.2960804910603665
Kurtosis MACD  (12,26,9): 2.261792896502783
Kurtosis Signal MACD (12,26,9): 2.5078141283806827
Kurtosis MACD (12,26,9)_hist: 0.05811870967763921
Kurtosis Volume: 7.635372407052374
