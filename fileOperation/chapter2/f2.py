# サブフォルダ内のファイルも対象にする
from pathlib import Path

current = Path()
for path in current.glob('**/*.jpg'):
    print(path)

# **/を追加することでサブフォルダも含めて探す