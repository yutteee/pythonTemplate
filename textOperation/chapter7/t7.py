# 部分文字列の出現位置を調べる
txt = "Let's Program with Python"
wordpos = txt.find('Python')
print(txt)
print(' ' * wordpos + '^ここ')

# find(sub)メソッドはsubに指定した文字列を探す
# pythonでは文字列に整数をかけると文字列を繰り返しコピーできるため、pythonの出現位置まで半角スペースが並ぶ