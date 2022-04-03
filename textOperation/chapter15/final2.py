# 置換リストを作ってまとめて置換する
from pathlib import Path
txt = 'Windows版PythonをPowerShell実行'
path = Path('replist.csv')
csvtxt = path.read_text(encoding='utf-8')
lst = csvtxt.splitlines() #replist.csvを複数行に分割
for line in lst:
    words = line.split(',') # ,で分割
    txt = txt.replace(words[0], words[1])
print(txt)