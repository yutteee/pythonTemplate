# 累積和を求める
import pandas
from pathlib import Path
path = Path('sample.csv')
df = pandas.read_csv(path, index_col=0)
df = df.cumsum()
print(df)

# 入出金の記録から現在の収益を求めたい場合は個々の入金、出金を足していく必要があり、これを累積和という
# cumsumメソッドでイケる