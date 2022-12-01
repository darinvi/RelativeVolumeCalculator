from relative_volume import RelativeVolumeMain
from historical_data_prep import historicalDataFrame
import regression as reg

def initVariables(symbol):
    # rvol = RelativeVolumeMain(symbol)
    rvol = 2
    df = historicalDataFrame(symbol)
    return rvol,df

def main():
    symbol = input("Symbol: ").upper()
    rvol,df = initVariables(symbol)
    reg_fit = reg.regression(df,'RR','Rvol')
    nl = '\n'
    def newAction():
        action = int(input(f"{nl}Press number for action:{nl}1. New symbol{nl}2. Show RVOL{nl}3. Show regression fit{nl}4. Show plot{nl}5. Show expected Range{nl}6. Quit{nl}"))
        if action == 1:
            main()
        elif action == 2:
            print(f"RVOL = {rvol}")
            newAction()
        elif action == 3:
            print(reg_fit.summary())
            newAction()
        elif action == 4:
            reg.showPlot(df)
            newAction()
        elif action == 5:
            reg.calculateExpectedRange(reg_fit,rvol,df)
            newAction()
        elif action == 6:  
            quit()
        else:
            print("Invalid input")
            newAction()
    newAction()

main()