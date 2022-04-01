# ファイルやフォルダの名前を変更する
from pathlib import Path

current = Path()
for path in current.glob('*.txt'):
    target = f'{path.stem}.TXT'
    path.rename(target)

# txt->TXTに変換するコード
# renameはフォルダやファイルの名前を変更する。フォルダ/ファイルみたいにすればファイルの移動もできる