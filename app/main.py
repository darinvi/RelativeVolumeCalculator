from relative_volume import RelativeVolumeMain
from historical_data_prep import historicalDataFrame
import calculations as cl

while True:
    symbol = input("Symbol: ").upper()
    rvol = RelativeVolumeMain(symbol)
    df = historicalDataFrame(symbol)
    cl.regression(df,'RR','Rvol')