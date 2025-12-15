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
    
