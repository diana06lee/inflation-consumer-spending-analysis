# inflation-consumer-spending-analysis

# Overview
This project analyzes how American consumers responded to post-pandemic inflation through comparing CPI (price changes) anad PCE (spending changes) across categories from 2021-2026, using the Federal Reserve economic data.

# Key Finding 
Energy prices were elastic and spiked enormously, but consumers cut back and prices were gradually corrected. Food, shelter, and non-durable goods were inelastic, meaning that prices rose steadily but consumers kept spending anyway.

# Tools Used
Python (pandas, matplotlib, fredapi)
FRED API (Federal Reserve Economic Data) 

## Files
- consumeranalysis.py — main analysis script
- cpi_chart.png — inflation by category since Jan 2021
- pce_chart.png — consumer spending by category since Jan 2021
- combined_chart.png — side by side comparison of CPI vs PCE

## Data Sources
- CPI data: U.S. Bureau of Labor Statistics via FRED
- PCE data: U.S. Bureau of Economic Analysis via FRED
