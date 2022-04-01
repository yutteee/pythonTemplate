# ファイル名や拡張子を取り出す
from pathlib import Path

current = Path()
for path in current.glob('*.*'):
    print(path.suffix)

# 存在するファイルの拡張子だけを表示するコード
# suffixは接尾辞を表す
# 同様にstemは接頭辞を表す