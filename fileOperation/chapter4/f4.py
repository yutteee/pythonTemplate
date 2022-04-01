# テキストファイルにテキストを追加する
from pathlib import Path

path = Path('テキスト2.txt')
txt = 'おうおうおうおうおうおうおwwwwwww'
path.write_text(txt, encoding='utf-8')

# pathオブジェクトのwrite_textメソッドを使うことでファイルに文字列を書き込むことができる