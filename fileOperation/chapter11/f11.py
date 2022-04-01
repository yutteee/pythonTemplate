# ファイルを削除する
from pathlib import Path
path = Path('a_dir/ant.TXT')
path.unlink()

# unlinkメソッドはファイルを削除することができる。フォルダはmkdirを使うらしい。