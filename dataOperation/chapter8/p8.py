# 行、列ごとの合計を求める
import pandas
from pathlib import Path
path = Path('sample1.csv')
df = pandas.read_csv(path, parse_dates=['日付'], thousands=',')
ttl = df.sum(axis=1)
print(ttl)

# 引数axisに1を指定した場合は横方向、0を指定した場合は縦方向