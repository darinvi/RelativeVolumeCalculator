import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

def regression(df,dep,indep):
    result = sm.ols(formula=f'{dep} ~ {indep}',data=df).fit()
    return result

def showPlot(df):
    df.plot.scatter(x="Rvol",y="RR")
    plt.show()

def calculateExpectedRange(fit,rvol,df):
    intercept,coef = fit.params
    atr_today = df['ATR'][-1]
    print(f"E(TR): {intercept:.2f} + {coef:.2f} * {rvol:.2f} = {intercept+coef*rvol*atr_today:.2f}")
    print(f"Expected Range today: {intercept+coef*rvol:.2f} times the Average True Range ({atr_today})")