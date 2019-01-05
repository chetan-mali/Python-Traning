#Create a function count letter,word and  line of a text file
import os

def wc(file):
    Line_count = 0
    word_count = 0
    character_count =0

    List = file.readlines()
    for element in List:
        character_count+=len(element)
        word_count+=len(element.split())
    file.seek(0,0)
    List2 = file.read()
    unique_word = set(List2.split())
    print("Lines :",len(List))
    print("Words :",word_count)
    print("Character :",character_count)
    print("Unique_word :",len(unique_word))
while(True):
    try:
        path ="C:/Users/Minicoder/Desktop/Forsk Technologies/code challenge"
        list_file = os.listdir(path)
        print("All files in current Directory :")
        for file in list_file:
            print("    ",file)
        filename = input("Enter name of file :")
        file = open(filename,"r")
        wc(file)
    except Exception as e:
        print(e)
    else:
        break