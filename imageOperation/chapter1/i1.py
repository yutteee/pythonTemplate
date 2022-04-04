# 画像ファイルを開く
from PIL import Image
from pathlib import Path
path = Path('image1.jpg')
img = Image.open(path)
print(img.width, img.height)