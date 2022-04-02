# 古いファイルをサブフォルダの中に片付ける
from pathlib import Path
from shutil import move
from datetime import datetime

current = Path()
target = Path('old')
target.mkdir(exist_ok=True)
today = datetime.today()
untilday = datetime(today.year, today.month, 1) #今日の日付の年、月を取得してその月の１日を指定

for path in current.glob('*.txt'):
    st_mtime = path.stat().st_mtime #更新日時の情報を取得
    update = datetime.fromtimestamp(st_mtime)
    if update < untilday:
        move(str(path), str(target))