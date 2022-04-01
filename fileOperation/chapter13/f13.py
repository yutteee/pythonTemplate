# フォルダを作成する
from pathlib import Path
path = Path('c_dir')
path.mkdir(exist_ok=True)

# mkdirメソッドでフォルダを作成
# 引数exist_okにTrueを指定するとすでに同名のフォルダがあってもエラーにしない。