# 文字列を行ごとに分割したリストにする
from encodings import utf_8
from pathlib import Path
path = Path('sample.txt')
txt = path.read_text(encoding='utf_8')
lst = txt.splitlines()
for line in lst:
    print('>>>', line)

# テキストファイルを一行づつ処理したい場合に役立つのがstr.splitlinesメソッド