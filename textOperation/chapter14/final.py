# フォルダ内のテキストファイルをすべて置換処理して保存する
from pathlib import Path
current = Path()
target = Path('result')
target.mkdir(exist_ok=True)

for path in current.glob('*.txt'):
    txt = path.read_text(encoding='utf-8')
    txt = txt.replace('python', 'パイソン')
    tpath = target / path #元のファイルを上書きしないためにresultファイルに置換したのをコピー
    tpath.write_text(txt, encoding='utf-8')