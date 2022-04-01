# テキストファイルを読み込む
from pathlib import Path

path = Path('テキスト1.txt')
txt = path.read_text(encoding='utf-8')
print(txt)

# Pathオブジェクトのread_textメソッドを使うことでテキストファイルの内容を読み込むことができる