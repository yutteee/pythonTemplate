# itertoolsを使って多重ループを簡潔に書く
from itertools import product
for x, y in product(range(1, 10), range(1, 10)):
    print(f'{x}*{y}={x*y}')

# itertoolsは繰り返し処理のための便利な関数をまとめたモジュール
# product関数は複数のオブジェクトからデカルト積のオブジェクトを作り出す