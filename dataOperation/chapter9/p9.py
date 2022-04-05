# 辞書データからDataFrameオブジェクトを作る
import pandas
dct = {
    '東京店': [1230700, 1700400, 657500],
    '大阪店': [1615350, 1350200, 320990]
}
df = pandas.DataFrame(dct)
print(df)

# DataFrameコントラスタを使うとDataFrameオブジェクトを作れる