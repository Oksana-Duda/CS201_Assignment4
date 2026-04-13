import pandas as pd
import numpy as np

df = pd.read_csv('random_walk.csv')
df['distance'] = (df['x']**2 + df['y']**2)**0.5
max_len = max(df['distance'].values)
avg_len = df['distance'].sum() / (max(df['step'])+1)
print(max_len, avg_len)
max_table = df[df['distance']>avg_len]
print(max_table)
max_table.to_json('filtered_walk.json', orient='records', lines=True)