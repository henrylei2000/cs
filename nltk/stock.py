import yfinance as yf   # lxml is required for the functions

from pandas_datareader import data as pdr
import datetime
import yfinance as yf
import pandas as pd


def get_data(ticker, start_date, end_date):
    delta = 999
    market_closed = True
    try:
        while market_closed:

            data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)

            if len(data['Adj Close']) < 2:
                if len(data['Adj Close']) == 0:
                    start_date += datetime.timedelta(days=1)
                    end_date += datetime.timedelta(days=1)
                elif len(data['Adj Close']) == 1:  # not end_date data
                    end_date += datetime.timedelta(days=1)
            else:
                market_closed = False
        delta = 100 * (data['Adj Close'][1] - data['Adj Close'][0]) / data['Adj Close'][0]
    except KeyError:
        pass

    return delta


def save_data(df, filename):
    # df.to_csv('./data/'+filename+'.csv')
    # for i in range(0, 11):
    #     df1 = pd.read_csv('./data/' + str(files[i])+'.csv')
    # print(df1.head())
    pass



def get_stocks():
    # yf.pdr_override()
    # Tickers list
    ticker_list = ['^GSPC', '^IXIC', 'AAPL']
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    # We can get data by our choice by giving days bracket
    start_date = "2020-09-01"
    end_date = "2020-09-01"
    files = []

    # This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
    for tik in ticker_list:
        get_data(tik, yesterday, today)


def main():
    get_stocks()


if __name__ == "__main__":
    main()
