# 先頭が特定の単語で始まるかチェックする
lst = ['鏡花水月', '流刃若火', '天鎖斬月', '千本桜景厳']
for txt in lst:
    if txt.startswith('鏡花'):
        print(txt)

# startswithメソッドは特定の文字列で始まるかをチェックする