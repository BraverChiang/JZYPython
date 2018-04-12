# 42 pillow. 43, 44, 45, 46, 47, 48.

from PIL import Image

image = Image.open("77.jpg")
print(image.size)
print(image.format)

area = (100,100,200,100)
cropped_image = image.crop(area)

# image2 = Image.open("2.jpg")
# area2 = (100,100,300,300)
# image2.paste(image, area2) #

r, g, b = image.split()
r.show()
g.show()
b.show()

new_image = Image.merge("RGB", (r, g, b))

square_image = image.resize((200, 200))
flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
spin_image = image.transpose(Image.ROTATE_90)

image.show()
square_image.show()
flip_image.show()
spin_image.show()

from PIL import ImageFilter
blur_image = image.filter(ImageFilter.BLUR)
detail_image = image.filter(ImageFilter.DETAIL)
edges_image = image.filter(ImageFilter.FIND_EDGES)

blur_image.show()
detail_image.show()
edges_image.show()

