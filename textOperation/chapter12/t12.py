# パターンにマッチするものをすべて見つける
import re
txt = '郵便番号は120-0021と201-0105'
lst = re.findall(r'\d{3}-\d{4}', txt)
print(lst)

# パターンに一致するものをリストで返すre.findall関数