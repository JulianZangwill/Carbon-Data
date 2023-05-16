import pandas as pd
from line_plot import line_plot

df = pd.read_excel(f'Excel_files\\Bloomberg_Data.xlsx', dtype=str)

df = df.dropna(axis=0, how='all')
df = df.dropna(axis=1, how='all')
heading = df.iloc[0:2]
df = df.iloc[2:]

heading = heading.fillna(axis=1, method='ffill')
heading = heading.fillna(value='')
df.columns = pd.MultiIndex.from_frame(heading.transpose())

df['', 'Date'] = pd.to_datetime(df['', 'Date'], format='%m/%d/%Y', errors='coerce').fillna(
    pd.to_datetime(df['', 'Date'], format='%Y-%d-%m 00:00:00', errors='coerce')
)
df = df.set_index(df['', 'Date']).drop('Date', axis=1, level=1)
df.index.name = 'Date'
df.columns.names = [None, None]

for name, item in df.columns[1:]:
    if item == 'Last Px':
        print(f'Processing {name}')
        single = df[name, 'Last Px'].dropna(how='any').astype('Float64')
        line_plot(single, f'{name}_JJ')
