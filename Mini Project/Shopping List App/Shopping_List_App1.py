"""
Shopping List App1
We are going to make a “Shopping List” app.
Run the script to start using it.
Put new things into the list one at a time
Enter the word DONE - in all CAPS - to QUIT the program
And once i quit, I want the app to show me everything thats on my list.
"""
shoping_list = []
while True :
    Item = input("Enter Item:")
    if Item == "DONE":
        break
    shoping_list.append(Item)
print("Shoping list !!!")
for items in shoping_list:
    print("  ",items)
