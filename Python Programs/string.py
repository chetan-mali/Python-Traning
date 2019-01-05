while(True):
    try:
        name = input("Enter name :")
        lst = name.split()
        if(len(lst)<2):
            raise ValueError("Only one name Entered !!")
    except Exception as e:
        print("Invalid Input !!", e)
    else:
        break

index = name.index(' ')
print(name[index:],name[0:index])