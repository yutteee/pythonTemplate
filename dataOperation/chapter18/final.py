# 一ヶ月分の日付をexcelファイルに書き出す
import pandas
from pathlib import Path
from datetime import datetime
today = datetime.today()
start = datetime(today.year, today.month, 1)
endm = today.month % 12 + 1 #単純に月に１を足すと13月ができちゃうかもしれない
end = datetime(today.year, endm, 1)
dti = pandas.date_range(start, end, freq='1D')
df = pandas.DataFrame(dti)
print(df)
path = Path('www.xlsx')
df.to_excel(path, index=False)