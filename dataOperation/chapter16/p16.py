# グラフの軸の書式を設定する
import pandas
import matplotlib.pyplot as plt
from matplotlib import ticker
from pathlib import Path
path = Path('sample.csv')
df = pandas.read_csv(path, parse_dates=['Date'], index_col=0, thousands=',')
ax = df.plot()
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
plt.show()

# yaxisはy軸のこと
# set_major_formatterはメモリの設定をしろって感じのメソッド
# {x:.0f}は変数xを小数点以下なしで表示するという意味