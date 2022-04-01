# ファイル名をパターンマッチする
from pathlib import Path

current = Path()
for path in current.glob('*'):
    if path.match('a*'):
        print(path)

# matchメソッドを使うことでパターンに一致するかチェックするメソッド
# 今回はaで始まるファイルを表示する
# macでは大文字と小文字を区別しない