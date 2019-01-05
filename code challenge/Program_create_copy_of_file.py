import os
import shutil
while(True):
    try:
        path ="C:/Users/Minicoder/Desktop/Forsk Technologies/code challenge"
        list_file = os.listdir(path)
        print("All files in current Directory :")
        for file in list_file:
            print("    ",file)
        filename = input("Enter name of file you want to copy :")
        new_filename= "copy_"+filename
        shutil.copy(filename,new_filename)
    except Exception as e:
        print(e)
    else:
        break
print("Copy Successfull !!")