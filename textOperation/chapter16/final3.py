# ファイルを拡張仕事に整理する処理をパワーアップ
from pathlib import Path
from shutil import copy
current = Path()
for path in current.glob('*.*'):
    if path.match('*.py'):
        continue
    ext = path.suffix
    ext = ext.lower()[1:] # lower()メソッドで小文字化、１文字目から取り出す
    target = Path(ext)
    target.mkdir(exist_ok=True)
    copy(str(path), str(target))
    tpath = target / path # pathの拡張子を取り除いているのでフォルダに入ったあとrename
    npath = target / Path(path.stem + '.' + ext)
    tpath.rename(npath)