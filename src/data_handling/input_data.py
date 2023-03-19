import pandas as pd
import pydantic

def read_config(path:str, data_model) -> pydantic.BaseModel:
    pass

def read_file(path:str, columns:list=None) -> pd.DataFrame:
    return pd.read_csv(path, usecols=columns, header=0, index_col=False, sep=',')
