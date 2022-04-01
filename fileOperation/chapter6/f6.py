# ファイル化フォルダかを見分ける
from pathlib import Path

current = Path()
for path in current.glob('*'):
    if path.is_dir():
        print(f'{path}フォルダ')

# pathオブジェクトのis_dirメソッドはフォルダだった場合trueを返すメソッド
