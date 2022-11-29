import finnhub
import datetime,pytz,time

def client(symbol):
    #returns time series for open,high,low,close,volume,time
    epoch = int(time.time())
    client = finnhub.Client(api_key="caq8suiad3iecj6adq7g")
    data = client.stock_candles(symbol,"1",epoch-2000000,epoch)
    return data

def main(symbol):
    candles = getVolumeAndTime(symbol)
    candles = mapUnixToDate(candles)
    candles = getRegularTradingSession(candles)
    calculateRelativeVolume(candles)
    
def getVolumeAndTime(symbol):
    #only returns volume and time for the purposes of this program
    data = client(symbol)
    if not len(data['t']) == len(data['v']):
        print("finnhub wrong response")
        #add recursion to main here
    filtered = [element for element in list(map(list,zip(list(data['v']),list(data['t']))))]
    return filtered

def unixToNyDate(lst_element):
    #finnhub returns unix, much easier to filter based on hour and minute.
    ny_timezone = pytz.timezone('America/New_York')
    unix_to_datetime = datetime.datetime.utcfromtimestamp(lst_element[1]).replace(tzinfo=pytz.utc)
    as_date = unix_to_datetime.astimezone(ny_timezone)
    lst_element[1] = as_date
    return lst_element

def mapUnixToDate(lst):
    lst = list(map(unixToNyDate,lst))
    return lst

def getRegularTradingSession(lst):
    #this one fillters data for the whole trading session.
    regular_session = [rs for rs in lst if \
        (rs[1].hour==9 and rs[1].minute>29) or rs[1].hour in range(10,16)]
    #this one fillters it up to the current moment.
    current_time = [ct for ct in regular_session if \
        ct[1].hour<lst[-1][1].hour or (ct[1].hour==lst[-1][1].hour and ct[1].minute<=lst[-1][1].minute)]
    return current_time

def separateData(lst):
    #separate today's data from data for the past days so I can compare
    #Only returns closes
    rolling_days = list(dict.fromkeys([days[1].day for days in lst]))[-11:-1]
    past_closes = [item[0] for item in lst if item[1].day in rolling_days]
    today_closes = [item[0] for item in lst if item[1].day==lst[-1][1].day]
    return past_closes,today_closes

def calculateAverageVolume(lst):
    print(sum(lst))
    return sum(lst)/len(lst)

def calculateRelativeVolume(lst):
    past,today = separateData(lst)
    past_avg = calculateAverageVolume(past)
    today_avg = calculateAverageVolume(today)
    rvol = today_avg/past_avg
    print(f"RVOL = {rvol}")

while True:
    symbol = input("Symbol: ").upper()
    main(symbol)