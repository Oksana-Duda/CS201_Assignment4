import pandas as pd
import numpy as np

df = pd.read_csv('random_walk.csv')
df['distance'] = (df['x']**2 + df['y']**2)**0.5
