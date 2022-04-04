# 拡張子別にファイルを集計する
from pathlib import Path
dct = {}
current = Path()
# 拡張子があるときは+1、拡張子がないときは新しく作って１を設定
for path in current.glob('**/*.*'):
    ext = path.suffix
    if ext in dct:
        dct[ext] += 1
    else:
        dct[ext] = 1
    print(dct)
for key, value in dct.items():
    print(f'{key}は{value}個')