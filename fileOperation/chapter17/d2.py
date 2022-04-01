# 日付データを指定した書式の日付文字列にする
from datetime import datetime
today = datetime.today()
datestr = f'{today:%Y/%m/%d}'
print(datestr)
# 変数:日付の表示文字列というフォーマット文字列を使うと任意の形式で日付文字列を作成できる