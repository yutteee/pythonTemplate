# 抜けた値を補間する
import pandas
from pathlib import Path
path = Path('sample.csv')
df = pandas.read_csv(path, index_col=0)
df = df.interpolate()
print(df)

# 前後のデータを参考に値を保管するinterpolateメソッド