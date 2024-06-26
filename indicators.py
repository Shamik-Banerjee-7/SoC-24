import yfinance as yf

ticker = "AAPL"
data = yf.download(ticker,start = "2021-01-01", end = "2024-01-01")

import pandas as pd
import numpy as np

#collection and processing

data.to_csv('historical_stock_data.csv')
data = pd.read_csv('historical _stock_data.csv',index_col = "Date",parse_dates=True)
data = data.dropna()

#plotting 20 day moving average vs 50 day moving average

data['20_MA'] = data['Close'].rolling(window = 20).mean()
twenty_moving_list = data['20_MA'].tolist()
data['50_MA'] = data['Close'].rolling(window = 50).mean()
fifty_moving_list = data['50_MA'].tolist()

import matplotlib.pyplot as plt
plt.plot(data['20_MA'],"r-")
plt.plot(data['50_MA'],'b-')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

#plotting the RSI 

condition = data['Close'].diff() >=0
condition_2 = data['Close'].diff() <0
data['Points_Gained'] = np.where(condition,data['Close'].diff(),0)
data['Points_Lost'] = np.where(condition_2,data['Close'].diff(),0)
data['RSI'] = 100*(1-((abs(data['Points_Lost'].rolling(window = 14).sum()/14))/((abs(data['Points_Lost'].rolling(window = 14).sum()/14)) + (data['Points_Gained'].rolling(window = 14).sum()/14))))
plt.plot(data['RSI'],"g-")
plt.show()