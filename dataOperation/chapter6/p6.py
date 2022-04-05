# 表の行と列を転置する
import pandas
from pathlib import Path
path = Path('sample2.csv')
df = pandas.read_csv(path, index_col=0)
dft = df.T
print(dft)

# DataFrame.Tプロパティを使うことで行と列を入れ替えることができる