import os
from PIL import Image
from PIL.ExifTags import TAGS
from exif import Image

with open("C:/Research/Dataset/mirflickr25k/Dataset/test.jpg","rb")as img1_file:
    img1 = Image(img1_file)

with open("C:/Research/Dataset/mirflickr25k/Dataset/im159.jpg","rb")as img2_file:
    img2 = Image(img2_file)
with open("C:/Research/Dataset/mirflickr25k/Dataset/im1817.jpg", "rb")as img3_file:
   img3 = Image(img3_file)
image_list = [img1,img2,img3]

for image in enumerate(image_list):
    if image.has_exif():
        update = f"contains EXIF information"
        print(f"Image{update}")
