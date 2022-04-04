# テキストファイルを行ごとに並べ替えて保存する
from pathlib import Path
path = Path('yougo.txt')
txt = path.read_text(encoding='utf-8')
lst = txt.splitlines()
lst.sort() #key=str.lowerを引数に指定すると大文字と小文字の区別なく並べる
txt = '\n'.join(lst)
path = Path('yougo_w.txt')
path.write_text(txt, encoding='utf-8')