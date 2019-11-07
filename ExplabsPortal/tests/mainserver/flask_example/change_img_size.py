from PIL import Image
img = Image.open("static/img/cards/dvwa.jpg")
width, height = img.size
print(width, height)
area = (0, 0, 1600, 900)
cropped_img = img.crop(area)
cropped_img.show()
