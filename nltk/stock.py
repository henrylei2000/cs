import yfinance as yf   # lxml is required for the functions

from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd


# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list = ['^GSPC', '^IXIC', 'AAPL']
today = date.today()

# We can get data by our choice by giving days bracket
start_date = "2020-09-01"
end_date = "2020-09-30"
files = []


def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    dataname = ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)


# Create a data folder in your current dir.
def SaveData(df, filename):
    #df.to_csv('./data/'+filename+'.csv')
    print(df)



#This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
for tik in ticker_list:
    getData(tik)

# for i in range(0, 11):
    #     df1 = pd.read_csv('./data/' + str(files[i])+'.csv')
    # print(df1.head())


# msft = yf.Ticker("AAPL")
# print(msft)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
# print(msft.info)

"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}
"""

# get historical market data, here max is 5 years.
# print(msft.history(period="max"))
"""
returns:
              Open    High    Low    Close      Volume  Dividends  Splits
Date
1986-03-13    0.06    0.07    0.06    0.07  1031788800        0.0     0.0
1986-03-14    0.07    0.07    0.07    0.07   308160000        0.0     0.0
...
2019-11-12  146.28  147.57  146.06  147.07    18641600        0.0     0.0
2019-11-13  146.74  147.46  146.30  147.31    16295622        0.0     0.0
"""