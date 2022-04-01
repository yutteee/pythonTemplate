# ファイルの最終更新日時を調べる
from pathlib import Path
from datetime import datetime
path = Path('ant.TXT')
st_mtime = path.stat().st_mtime
update = datetime.fromtimestamp(st_mtime)
print(update)

# pathオブジェクトのstatメソッドで情報を取得する
# st_mtimeは更新日時を表す
# datetime.frontimestampはタイムスタンプから作成を表す