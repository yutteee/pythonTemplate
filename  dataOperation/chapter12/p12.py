# 日付の連続データを作る
import pandas
dti = pandas.date_range('2020-4-1', periods=4, freq='7D')
dct = {'週': [1, 2, 3, 4]}
df = pandas.DataFrame(dct, index=dti)
print(df)

# 連続する時刻のデータを作成できるdate_range関数
# 引数freqに指定した7Dは7daysってこと
# 引数periodsは生成する数（回数)