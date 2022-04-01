# ファイルが存在するかチェックする
from pathlib import Path

path = Path('スタップ細胞.txt')
if path.exists():
    print(f'{path}はあります')
else:
    print(f'{path}はありません')

# path.exsistsメソッドはpathオブジェクトが示すファイルが存在するときにtrueを返すメソッド