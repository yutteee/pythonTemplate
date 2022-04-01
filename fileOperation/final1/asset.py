# ファイルを拡張子ごとに整理する
from pathlib import Path
from shutil import copy

current = Path()
for path in current.glob('*.*'):
    if path.match('*.py'):
        continue #pythonファイルは分類しない
    ext = path.suffix #取得したファイル名の接尾字
    target = Path(ext) #それにpathを通す
    target.mkdir(exist_ok=True) #フォルダを作成
    copy(str(path), str(target)) #targetを指定してコピー
