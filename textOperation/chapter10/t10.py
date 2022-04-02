# ゼロで埋めて桁揃えする
lst = ['192', '168', '1', '24']
for txt in lst:
    txt = txt.zfill(3)
    print(txt)

# 先頭に0をつけて桁を揃えることをゼロ埋めやゼロパディングという
# zfillメソッドを使う
