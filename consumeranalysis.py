#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:36:48 2026

@author: dianalee
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from fredapi import Fred

# Connect to FRED
fred = Fred(api_key='7dd16f3d49b0e24ca0d5954de9d238ac')

# Pull CPI by category (2021-2026)
series = {
    'All Items':    'CPIAUCSL',
    'Food at Home': 'CPIFABSL',
    'Food Away':    'CUSR0000SEFV',
    'Energy':       'CPIENGSL',
    'Shelter':      'CUSR0000SAH1',
    'Apparel':      'CPIAPPSL',
    'Medical Care': 'CPIMEDSL',
}

# Download each series
data = pd.DataFrame()
for name, code in series.items():
    s = fred.get_series(code, observation_start='2021-01-01', observation_end='2026-01-01')
    data[name] = s

# Convert to % change from Jan 2021 baseline
baseline = data.iloc[0]
pct_change = ((data - baseline) / baseline) * 100

# Plot CPI
plt.figure(figsize=(12, 6))
for col in pct_change.columns:
    plt.plot(pct_change.index, pct_change[col], label=col)

plt.title('CPI % Change by Category Since Jan 2021')
plt.xlabel('Date')
plt.ylabel('% Change from Jan 2021')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
ax = plt.gca()
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('/Users/dianalee/Desktop/cpi_chart.png', dpi=150, bbox_inches='tight')
print("CPI chart saved!")

# Pull PCE by category
pce_series = {
    'Durable Goods':    'PCEDG',
    'Nondurable Goods': 'PCEND',
    'Services':         'PCESV',
    'Food & Beverage':  'DFXARC1M027SBEA',
}

pce_data = pd.DataFrame()
for name, code in pce_series.items():
    try:
        s = fred.get_series(code, observation_start='2021-01-01', observation_end='2026-01-01')
        pce_data[name] = s
        print(f"✓ {name}")
    except:
        print(f"✗ {name} — skipping")

# Convert to % change from Jan 2021
pce_baseline = pce_data.iloc[0]
pce_pct = ((pce_data - pce_baseline) / pce_baseline) * 100

# Plot PCE
plt.figure(figsize=(12, 6))
for col in pce_pct.columns:
    plt.plot(pce_pct.index, pce_pct[col], label=col)

plt.title('PCE (Consumer Spending) % Change by Category Since Jan 2021')
plt.xlabel('Date')
plt.ylabel('% Change from Jan 2021')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
ax = plt.gca()
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('/Users/dianalee/Desktop/pce_chart.png', dpi=150, bbox_inches='tight')
print("PCE chart saved!")





# Combined CPI vs PCE chart (side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Left side: CPI
for col in pct_change.columns:
    ax1.plot(pct_change.index, pct_change[col], label=col, linewidth=2)
ax1.set_title('Inflation (CPI) by Category', fontsize=14, fontweight='bold')
ax1.set_xlabel('Date', fontsize=11)
ax1.set_ylabel('% Change from Jan 2021', fontsize=11)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Right side: PCE
for col in pce_pct.columns:
    ax2.plot(pce_pct.index, pce_pct[col], label=col, linewidth=2)
ax2.set_title('Consumer Spending (PCE) by Category', fontsize=14, fontweight='bold')
ax2.set_xlabel('Date', fontsize=11)
ax2.set_ylabel('% Change from Jan 2021', fontsize=11)
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig.suptitle('Inflation vs Consumer Spending: 2021–2026', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('/Users/dianalee/Desktop/combined_chart.png', dpi=150, bbox_inches='tight')
print("Combined chart saved!")






