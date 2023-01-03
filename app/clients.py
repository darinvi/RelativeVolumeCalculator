import finnhub,time,datetime
import pandas_datareader.data as web
import yfinance as yf

def finnhubClient(symbol):
    #returns time series for open,high,low,close,volume,time
    epoch = int(time.time())
    client = finnhub.Client(api_key="caq8suiad3iecj6adq7g")
    data = client.stock_candles(symbol,"1",epoch-4000000,epoch)
    return data

def yahooClient(symbol):
    yf.pdr_override()
    start = datetime.datetime(2000,1,1)
    end = datetime.datetime(2022,12,31)
    df = web.get_data_yahoo(symbol,start, end)
    return df
