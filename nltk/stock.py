import yfinance as yf   # lxml is required for the functions

from pandas_datareader import data as pdr
import datetime
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


def get_stock(ticker, start, day):
    print(start)
    day_before = day - datetime.timedelta(days=1)
    getData(ticker, start, day)


def get_stocks():
    # Tickers list
    # We can add and delete any ticker from the list to get desired ticker live data
    # yf.pdr_override()

    ticker_list = ['^GSPC', '^IXIC', 'AAPL']
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    date_time_str = '18/09/19 01:55:19'

    date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
    print(date_time_obj)

    # We can get data by our choice by giving days bracket
    start_date = "2020-09-01"
    end_date = "2020-09-01"
    files = []

    # This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
    for tik in ticker_list:
        getData(tik, yesterday, today)


def main():
    get_stocks()


if __name__ == "__main__":
    main()
