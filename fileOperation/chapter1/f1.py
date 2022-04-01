# 拡張子がjpgのものだけを取り出す
from pathlib import Path

current = Path()
for path in current.glob('*.jpg'):
    print(path)

# globでpathを取得できる
# アスタリスク*はワイルドカードと呼び、すべての文字にマッチするという意味がある