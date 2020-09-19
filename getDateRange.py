import pandas as pd
from pandas import DataFrame

import datetime

df = pd.read_csv("data/ted.csv", index_col = 'Start Time', parse_dates = True)

print(df)
# df['date'] = df['Start Time'].dt.date

# mask = (df['date'] >= '2020-03-22') & (df['date'] <= '2020-03-25')

# mask.to_csv("data/ted-date.csv")
