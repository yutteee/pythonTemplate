# 正規表現を使ってパターンマッチをする
import re
txt = '120-0021'
if re.match(r'\d{3}-\d{4}', txt):
    print(f'{txt}は郵便番号だ')
else:
    print(f'{txt}は郵便番号ではない')

# re.match関数は文字列が正規表現のパターンにマッチしているかを調べる
# 正規表現パターンの\d{3}は数字３個を表す