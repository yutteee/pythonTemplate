# 画像を保存する
from PIL import Image
from pathlib import Path
path = Path('image1.jpg')
img = Image.open(path)
path = Path('image1.png')
img.save(path, dpi=(128, 128))