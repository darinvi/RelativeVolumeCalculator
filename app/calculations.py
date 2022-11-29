import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

def regression(df,dep,indep):
    showPlot(df)
    result = sm.ols(formula=f'{dep} ~ {indep}',data=df).fit()
    print(result.summary())

def showPlot(df):
    df.plot.scatter(x="RR",y="Rvol")
    plt.show()

def calculateExpectedRange(coefs,rvol):
    pass