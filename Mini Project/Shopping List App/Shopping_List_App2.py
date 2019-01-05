"""
Shopping List App2
We are going to make a “Shopping List” app.
Run the script to start using it.
Put new things into the list one at a time
Enter the word DONE - in all CAPS - to QUIT the program
And once i quit, I want the app to show me everything thats on my list.

If I type SHOW, I should be able to see what is currently in the list
If I type HELP, I should be able to see all the help for these special commands
"""

def Show(shopping_list):
    print("ItemsShoping list !!!")
    for items in shoping_list:
        print("  ", items)
def Help():
    print("Type SHOW to disply the current  shopping list")
    print("Enter the word DONE - in all CAPS - to QUIT the program")
shoping_list = []
while True :
    Item = input("Enter Item:")
    if Item == "DONE":
        Show(shoping_list)
        break
    elif Item=="SHOW":
        Show(shoping_list)
    elif Item == "HELP":
        Help()
    else:
        shoping_list.append(Item)

