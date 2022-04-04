# 食材の組み合わせで献立を考える
from pathlib import Path
from itertools import product
food = []
current = Path()
for path in current.glob('*.txt'):
    txt = path.read_text(encoding='utf-8')
    lst = txt.split(',')
    food.append(lst) # appendの引数にリストを指定するとリストの中にリストが入った状態になる
for tpl in product( *food ): # タプルやリストの引数の前に*をつけると展開した状態の引数として関数に渡される。これをアンパックという。
    print(tpl)