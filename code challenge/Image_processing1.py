"""
Image Processing : Rotate inage to 90
                   Convert to greyscale
                   Crop the image form center(w:160,h:204)
                   Apply thumbnail (75,75)
                   Also handle the Extension of image
"""
from PIL import Image
import os
while(True):
    try:
        path = "C:/Users/Minicoder/Desktop/Forsk Technologies/code challenge"
        list_file = os.listdir(path)
        Extension = [".png",".jpg",".jpeg",".bmp"]
        imagename = input("Enter Image Name:")
        for extn in Extension:
            if  imagename + extn in list_file:
                imagename = imagename + extn
        orignal = Image.open(imagename)
        orignal = orignal.convert("L")
        orignal = orignal.transpose(Image.ROTATE_90)
        width, height = orignal.size
        axis = ((width / 2) - 160, (height / 2) - 204, (width / 2) + 160, (height / 2) + 204)
        orignal = orignal.crop(axis)
        orignal.thumbnail((75, 75))
        orignal.show()
    except Exception as e:
        print("N")
    else:
        break
