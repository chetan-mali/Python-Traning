# Print final line of a textfile (take file name from user )
import os
while(True):
    try:
        path ="C:/Users/Minicoder/Desktop/Forsk Technologies/code challenge"
        list_file = os.listdir(path)
        print("All files in current Directory :")
        for file in list_file:
            print("    ",file)
        filename = input("Enter name of file :")
        file_open = open(filename,"r")
        List = file_open.readlines()
        print(List[-1])
    except Exception as e:
        print(e)
    else:
        break