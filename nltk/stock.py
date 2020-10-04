import yfinance as yf   # lxml is required for the functions

from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
import pandas as pd


def getData(ticker, start_date, end_date):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    dataname = ticker+'_'+str(end_date)
    #files.append(dataname)
    SaveData(data, dataname)


# Create a data folder in your current dir.
def SaveData(df, filename):
    # df.to_csv('./data/'+filename+'.csv')

    # for i in range(0, 11):
    #     df1 = pd.read_csv('./data/' + str(files[i])+'.csv')
    # print(df1.head())

    # df.columns = [''] * len(df.columns)
    print(df)


def get_stocks():
    # Tickers list
    # We can add and delete any ticker from the list to get desired ticker live data
    # yf.pdr_override()

    ticker_list = ['^GSPC', '^IXIC', 'AAPL']
    today = date.today()

    # We can get data by our choice by giving days bracket
    start_date = "2020-09-01"
    end_date = "2020-09-30"
    files = []

    # This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
    for tik in ticker_list:
        getData(tik, start_date, today)


def main():
    get_stocks()


if __name__ == "__main__":
    main()