# excelファイルを書き出す
import pandas
from pathlib import Path
path = Path('sample.csv')
df = pandas.read_csv(path)
path = Path('sample1x.xlsx')
df.to_excel(path, index=False)