import os
import shutil
while(True):
    try:
        path ="C:/Users/Minicoder/Desktop/Forsk Technologies/code challenge"
        list_file = os.listdir(path)
        print("All files in current Directory :")
        for file in list_file:
            print("    ",file)
        filename = input("Enter name of file you want to Read :")
        file_open = open(filename,"r")
        print(file_open.read())
    except Exception as e:
        print(e)
    else:
        break