import json
import pandas as pd 
import polars as pl 

f = open('data.json', 'r')
data = json.load(f)
df = pd.json_normalize(data, record_path=["data"])

marcasNames = df['marca_nombre'].tolist()
print(marcasNames)
print(df.head())
