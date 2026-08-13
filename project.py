#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:36:48 2026

@author: dianalee
"""

import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# connecting to FRED
fred = Fred(api_key='7dd16f3d49b0e24ca0d5954de9d238ac')

# pulling CPI by category (2021-2026)
series = {
    'All Items':    'CPIAUCSL',
    'Food at Home': 'CPIFABSL',
    'Food Away':    'CUSR0000SEFV',
    'Energy':       'CPIENGSL',
    'Shelter':      'CUSR0000SAH1',
    'Apparel':      'CPIAPPSL',
    'Medical Care': 'CPIMEDSL',
}

# downloading 
data = pd.DataFrame()
for name in series:
    code = series[name]
    data[name] = fred.get_series(code,observation_start='2021-01-01', observation_end='2026-01-01' )

first_value = data.iloc[0]
percent_change = (data - first_value) / first_value * 100


# plot
plt.figure(figsize=(12, 6))

for name in percent_change.columns:
    plt.plot(percent_change.index, percent_change[name], label=name)

plt.title('CPI % Change by Category Since Jan 2021')
plt.xlabel('Date')
plt.ylabel('% Change from Jan 2021')
plt.legend()
plt.grid()
plt.savefig('/Users/dianalee/Desktop/cpi_chart.png')

print("Chart saved!")

# Pull PCE by category (corrected series IDs)
pce_series = {
    'Durable Goods':     'PCEDG',
    'Nondurable Goods':  'PCEND',
    'Services':          'PCESV',
    'Food & Beverage':   'DFXARC1M027SBEA',
    'Energy':            'DTENRC1M027SBEA',
}

#getting data 
pce_data = pd.DataFrame()


for name in pce_series:
    code = pce_series[name]
    
    try:
        pce_data[name] = fred.get_series(code,observation_start='2021-01-01', observation_end='2026-01-01' )
        print(name, "loaded")
    except:
        print(name, "could not be loaded")
        
        
print(pce_data.head())



#percent change
first_pce_value = pce_data.iloc[0]
pce_percent_change = (pce_data- first_pce_value) / first_pce_value * 100



#plotting 
plt.figure(figsize=(12, 6))

for name in pce_percent_change.columns:
    plt.plot(pce_percent_change.index, pce_percent_change[name], label=name)
   

plt.title('PCE % Change by Category Since Jan 2021')
plt.xlabel('Date')
plt.ylabel('% Change From Jan 2021')
plt.legend()
plt.grid()
plt.savefig('/Users/dianalee/Desktop/pce_chart.png')
print("PCE chart saved!")




