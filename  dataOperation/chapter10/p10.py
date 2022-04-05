# 複数のDataFrameを連結する
import pandas
from pathlib import Path
path = Path('sample1.csv')
df = pandas.read_csv(path)
path = Path('sample3.csv')
df2 = pandas.read_csv(path)
df = pandas.concat([df, df2])
print(df)

# pandas.concat関数でDataFrameやSeriesを連結できる
# 引数axisで連結する方向を指定する