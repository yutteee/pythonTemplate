# csvファイル読み込み時に日付と数値を変換する
import pandas
from pathlib import Path
path = Path('sample1.csv')
df = pandas.read_csv(path, parse_dates=['日付'], thousands=',')
print(df['日付'])

# 引数parse_datesは日付データに変換したい列名のリスト
# 引数thousandsは数値を３桁区切りにするために使う文字列