# グラフを画像として保存する
import pandas
import matplotlib.pyplot as plt
from pathlib import Path
path = Path('sample.csv')
df = pandas.read_csv(path, parse_dates=['Date'], index_col=0, thousands=',')
df.plot()
path = Path('aaaa.png')
plt.savefig(path)

# savefigメソッドでグラフを画像として保存できる