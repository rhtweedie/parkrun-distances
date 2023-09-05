import pandas as pd

df = pd.read_csv('data/uk-parkruns.csv')

name = "Aberdeen"


def get_coords(name):
    return df[df['name'] == name]


print(df['lat'])
row = get_coords(name)
lat = row['lat']
