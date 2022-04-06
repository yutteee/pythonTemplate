# 複数のexcelファイルのデータを連結してグラフを作る
import pandas
import matplotlib.pyplot as plt
from pathlib import Path
current = Path()
dfmg = pandas.DataFrame()
for path in current.glob('*.xlsx'):
    if path.stem.startswith('~$'):
        continue #~$*.excelファイルはエクセルでファイルを開いているときに作られる一時ファイルで開くとエラー
    df = pandas.read_excel(path, sheet_name=0, header=0, index_col=1)
    srs = df['金額']
    srs.name = path.stem
    dfmg = pandas.concat([dfmg, srs], axis=1)
dfcs = dfmg.cumsum()
dfcs = dfcs.interpolate()
dfcs.plot()
plt.show()