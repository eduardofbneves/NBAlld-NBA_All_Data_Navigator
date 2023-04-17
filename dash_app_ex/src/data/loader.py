import pandas as pd

def load_dataframe(path: str) -> pd.DataFrame:
    '''This just loads the Dataframes as the .csv files are all aready treated'''
    data = pd.read_csv(path)
    return data
    