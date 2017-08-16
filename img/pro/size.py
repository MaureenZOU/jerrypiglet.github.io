from PIL import Image
import sys

img = Image.open(sys.argv[1])
new_img = img.resize((int(sys.argv[2]),int(sys.argv[3])))
new_img.save(sys.argv[1], "JPEG", optimize=True)