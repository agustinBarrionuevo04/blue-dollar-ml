import pandas as pd
import numpy as np 

class BaselineModels:
    def fit(self, x,y=None):
        pass

class AlwaysUp(BaselineModels):
    def predict_always_up(self, x):
        return np.ones(len(x))
    
class HowYesterday(BaselineModels):
    def predict_same_as_yesterday(self, x):
        return (x['lag_1'] > 0).astype(int).values
    



def get_rsi(data, periodo=14):
    delta = data['valor'].diff()
    delta = delta.dropna()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewn(com=periodo-1, adjust=False).mean()
    avg_loss = loss.ewn(com=periodo-1, adjust=False).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi

