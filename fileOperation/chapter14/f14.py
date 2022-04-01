# フォルダを削除する
from pathlib import Path
path = Path('c_dir')
path.rmdir()

# Path.rmdirメソッドはフォルダを削除するメソッド
# フォルダの中がからでなければ削除できないので先にunlinkメソッドでファイルを削除してからフォルダを削除する