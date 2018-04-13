from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont  # msgNum =str(random.randint(1,100))

im = Image.open('image/0.png')
# im.show()
w, h = im.size
font = ImageFont.truetype('arial.ttf', 50)
draw = ImageDraw.Draw(im)
draw.text((w-50, -10), '5', fill=(255, 10, 10), font=font)
# try:
im.save('01.png')  # except ValueError :
#     print("value error ")
