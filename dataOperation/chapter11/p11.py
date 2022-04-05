# 行や列を削除する
import pandas
from pathlib import Path
path = Path('sample1.csv')
df = pandas.read_csv(path)
df = df.drop('東京店', axis=1)
print(df)

# dropで指定した列または行を削除