import pandas as pd
import numpy as np

def check_nan_players(val) -> str:
    if pd.isnull(val):
        return '-----'
    elif type(val) == np.float64:
        return str(int(val))
    else:
        return str(val)
    