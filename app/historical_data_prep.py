import pandas as pd
from clients import yahooClient

def historicalDataFrame(symbol):
    df = yahooClient(symbol)
    df = addRelativeVolume(df)
    df = addTrueRanges(df)
    df = addAverageTrueRange(df)
    df = addRelativeRange(df)
    # using rolling window 20 so I prefer to clean the first entries that haven't cought up.
    df = df[20:]
    return df

def addRelativeVolume(df):
    # volume and average volume are numeric, relative volume is a coefficient showing how much volume is done today relative to the average for the day.
    df['Rvol'] = df['Volume']/df['Volume'].rolling(20,1).mean()
    return df

def addTrueRanges(df):
    # true range measures the range today, possibly relative to yestyerday prices if there is a gap.
    true_ranges = [0]
    for i in range(1,len(df['High'])):
        true_range_method_1 = abs(df['High'][i] - df['Low'][i])
        true_range_method_2 = abs(df['High'][i] - df['Close'][i-1])
        true_range_method_3 = abs(df['Low'][i] - df['Close'][i-1])
        true_ranges.append(max(true_range_method_1,true_range_method_2,true_range_method_3))
    df["TR"] = true_ranges
    return df

def addAverageTrueRange(df):
    # average of the true ranges for an arbitrary period (20 data points in this case).
    df["ATR"] = df["TR"].rolling(20,0,).mean()
    return df

def addRelativeRange(df):
    # range and atr are numeric, relative range is a coefficient. Same logic as relative volume.
    df["RR"] = df["TR"]/df["ATR"]
    return df