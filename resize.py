from PIL import Image
import pathlib

side = 100
maxsize = (side, side)
for input_img_path in pathlib.Path("map/6").iterdir():
    if 'DS_Store' in str(input_img_path):
        continue
    with Image.open(input_img_path) as im:
        w,h = im.size
        if (w,h) != maxsize:
            output_img_path = str(input_img_path).replace("/6/","/5/")
            im.thumbnail(maxsize)
            im.save(output_img_path, "png")

