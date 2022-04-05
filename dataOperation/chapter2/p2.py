# Excelファイルを読み込む
import pandas
from pathlib import Path
path = Path('sample1.xlsx')
df = pandas.read_excel(path, sheet_name=0, header=1)
print(df)

# pandas.read_excel関数でexcelファイルを読み込める