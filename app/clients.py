import finnhub
import time

def client(symbol):
    #returns time series for open,high,low,close,volume,time
    epoch = int(time.time())
    client = finnhub.Client(api_key="caq8suiad3iecj6adq7g")
    data = client.stock_candles(symbol,"1",epoch-2000000,epoch)
    return data