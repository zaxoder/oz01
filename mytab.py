import pandas as pd

df = pd.read_csv('dz.csv')

df.fillna(value=0, inplace=True)
grouped = df.groupby('City', as_index=False).agg({'Salary': 'mean'})

print(df)

print(grouped)

