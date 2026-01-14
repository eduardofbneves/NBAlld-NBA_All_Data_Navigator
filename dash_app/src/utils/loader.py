import pandas as pd
import os.path

def load_dataframe(file: str) -> pd.DataFrame:
    """Pass the file name and loads the csv into DataFrame

    Args:
        file (str): file name in the data folder

    Returns:
        pd.DataFrame: output DataFrame with the file info
    """    
    path = path_to_data(file)
    data = pd.read_csv(path)
    return data


def path_to_data(file: str) -> str:
    return os.path.join(os.getcwd(), 'data', file + '.csv')
    #return "./data/" + file + ".csv"