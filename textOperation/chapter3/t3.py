# 単語の出現数を調べる
from pathlib import Path
path = Path('sample.txt')
txt = path.read_text(encoding='utf-8')
cnt = txt.count('python')
print(cnt)

# sample.txtの中にあるpythonという文字列を数えるもの
# count(sub)メソッドは引数subに渡した文字列が何回登場するかを調べるメソッド