# csvファイルを書き出す
import pandas
from pathlib import Path
path = Path('sample.1.csv')
df = pandas.read_csv(path)
path = Path('sample1x.csv')
df.to_csv(path, index=False)

# csvファイルを書き出すにはDataFrame.to_csvオブジェクトを使う
# インでクックスを書き出さないのであれば、引数にindex=False