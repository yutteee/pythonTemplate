# 合計列をDataFrameオブジェクトに追加する
import pandas
from pathlib import Path
path = Path('sample.csv')
df = pandas.read_csv(path, parse_dates=['日付'], thousands=',')
ttl = df.sum(axis=1)
ttl.name = '計'
df = pandas.concat([df, ttl], axis=1)
print(df)