# ファイルやフォルダを移動する
from pathlib import Path
from shutil import move

path = Path('b_dir')
target = Path('a_dir')
move(str(path), str(target))
# shutilモジュールでファイルの移動やコピーなどができる
# move関数は第一引数に指定したファイルを第２引数に指定したフォルダ内に移動する