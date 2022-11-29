import finnhub
import time

def client(symbol):
    #returns time series for open,high,low,close,volume,time
    epoch = int(time.time())
    client = finnhub.Client(api_key="caq8suiad3iecj6adq7g")
    data = client.stock_candles(symbol,"1",epoch-1300000,epoch)
    return data

def getVolumeAndTime(symbol):
    #only returns volume and time for the purposes of this program
    data = client(symbol)
    if not len(data['t']) == len(data['v']):
        print("finnhub wrong response")
    filtered = [element for element in list(zip(list(data['v']),list(data['t'])))]
    return filtered

def getRegularTradingHours(data):
