# 1列分の合計を求める
import pandas
from pathlib import Path
path = Path('sample1.csv')
df = pandas.read_csv(path, parse_dates=['日付'], thousands=',')
srs = df('T京店')
ttl = sum(srs)
print(f'合計: {ttl}')

# df['列名']のように書くと一列分のSeriesオブジェクトを取り出す
# Seriesオブジェクトについて: https://deepage.net/features/pandas-series.html