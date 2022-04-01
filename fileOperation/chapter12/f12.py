# ファイルやフォルダをコピーする
from pathlib import Path
from shutil import copy

path = Path('ant.TXT')
target = Path('a_dir')
copy(str(path), str(target))
# shutilモジュールのcopy関数でファイルやフォルダをコピーできる
# move関数と基本的に使い方は同じ