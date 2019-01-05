from PIL import Image
import os
while(True):
    try:
        path = "H:\image"
        list_file = os.listdir(path)
        for file in list_file:
            print list_file
            if ".png" in file:
                image = Image.open(file)
                image.resize((100, 100))
                image.save(file)
    except Exception as e:
        print(e)
    else:
        break
print(pnglist)
