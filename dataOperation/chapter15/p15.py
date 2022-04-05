# DateFrameオブジェクトからグラフを作る
import pandas
import matplotlib.pyplot as plt
from pathlib import Path
path = Path('sample5.csv')
df = pandas.read_csv(path, parse_dates=['Date'], index_col=0, thousands=',')
df.plot()
plt.show()

# plotでグラフを作れる。日本語は文字化けしちゃうらしい。