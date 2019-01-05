# Calculate age
while(True):
    try :
        age = int(input("Enter Your age:"))
        if(age<0):
            raise ValueError("Age can't be nagetive !! ")
    except ValueError as e:
        print("Invalid input:",e)
    else:
        break
F_age = age + 5
P_age = age - 10
print("Your age after 5 year :", F_age)
if (P_age > -1):
    print("Your age 10 year back :", P_age)
else:
    print("You were not born !!")