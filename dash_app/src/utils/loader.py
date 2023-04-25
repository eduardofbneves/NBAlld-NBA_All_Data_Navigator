import pandas as pd
import os.path

def load_dataframe(file: str) -> pd.DataFrame:
    '''This just loads the Dataframes as the .csv files are all aready treated'''
    path = path_to_data(file)
    data = pd.read_csv(path)
    return data


def path_to_data(file: str) -> str:
    print(os.getcwd())
    return os.path.join(os.getcwd(), 'dash_app_ex', 'data', file + '.csv')
    #return "./data/" + file + ".csv"