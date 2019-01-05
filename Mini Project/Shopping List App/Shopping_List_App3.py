"""
[Shopping List App2]
We are going to make a “Shopping List” app.
Run the script to start using it.
Put new things into the list one at a time
Enter the word DONE - in all CAPS - to QUIT the program
And once i quit, I want the app to show me everything thats on my list.

If I type SHOW, I should be able to see what is currently in the list
If I type HELP, I should be able to see all the help for these special commands

User can enter SHOW or Show or show, similar for DONE and HELP, but the program should do the required job
Show the item in the list serially starting from 1
Let us accept items using a comma separated string
Also there should be a functionality to add an item at a specific index
There should be a functionality to remove items from the list at a specific index using REMOVE
Do all the exception handling for all the extreme use cases
"""

def Show(shopping_list):
    print("Shoping list !!!")
    i=0
    for items in shoping_list:
        print("  ",i,items.strip())
        i+=1
def Help():
    print("Type SHOW to disply the current  shopping list")
    print("Enter the word DONE - in all CAPS - to QUIT the program")
    print("REMOVE: type REMOVE and index number seperated with ','")
    print("ADD   : type ADD with index value and element seperated with ','")
f =open("shoping_list.txt","r+")

shoping_list = f.readlines()
while True :
    try:
        Item = input("Enter Item:").split(",")
        if '' in Item:
            raise Exception
        elif len(Item)==1:
            if Item[0].lower() == "done":
                Show(shoping_list)
                f = open("shoping_list.txt",'w')
                for elemeent in shoping_list:
                    f.write(elemeent+"\n")
                f.close()
                break
            elif Item[0].lower()=="show":
                Show(shoping_list)
            elif Item[0].lower() == "help":
                Help()
            else:
                shoping_list.append(Item[0])
        elif len(Item)== 2:
            if Item[0].upper() == "REMOVE" and Item[1].isdigit():
                if int(Item[1])<=len(shoping_list) and int(Item[1])>=0:
                    del(shoping_list[int(Item[1])])
                    print("Element removed !!!")
                else:
                    print("Invalid Index !!!")
            else:
                check = Item[1]
                if check[0]=="-" and check[1:].isdigit():
                    print("Invalid index !!")
                else:
                    shoping_list.append(Item[0])
                    shoping_list.append(Item[1])
        elif len(Item)==3:
            if Item[0].upper()=="ADD" and Item[1].isnumeric():
                if int(Item[1])<=len(shoping_list) and int(Item[1])>=0:
                    shoping_list.insert(int(Item[1]),Item[2])
                    print("Element added !!!")
                else:
                    print("Invalid Index !!!")
            else:
                check = Item[1]
                if check[0] == "-" and check[1:].isdigit():
                    print("Invalid index !!")
                else:
                    shoping_list.append(Item[0])
                    shoping_list.append(Item[1])
                    shoping_list.append(Item[2])
        else:
            for _ in Item:
                shoping_list.append(_)
    except Exception :
        print("Invaild Input !!!")