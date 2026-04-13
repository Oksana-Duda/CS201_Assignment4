import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('random_walk.csv')
df['distance'] = (df['x']**2 + df['y']**2)**0.5
max_len = max(df['distance'].values)
avg_len = df['distance'].sum() / (max(df['step'])+1)
print(max_len, avg_len)
max_table = df[df['distance']>avg_len]
print(max_table)
max_table.to_json('filtered_walk.json', orient='records', lines=True)


plt.figure(figsize=(8,4))
plt.plot(df['x'], df['y'], color='green', label=r"Траєкторія")
plt.title("Траєкторія блукання")
plt.scatter(0, 0, color='red', s=100, label="Початок")
end_x = df['x'][max(df['step'])]
end_y = df['y'][max(df['step'])]
plt.scatter(end_x, end_y, color='blue', s=100, label="кінець")
plt.xlabel('координата по х')
plt.ylabel('координата по y')
plt.legend()
plt.show()