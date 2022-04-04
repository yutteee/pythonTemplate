# csvファイルを読み込む
import pandas
from pathlib import Path
path = Path('sample1.csv')
df = pandas.read_csv(path)
print(df)

# read_csv関数を使うことでcsvファイルを読み込める
# 引数index_colは行見出しに使用する。指定がない場合は０から始まるインデックスが振られる