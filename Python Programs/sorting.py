List =[]
for _ in range(5):
    while(True):
        try:
            name,age,height = input("Enter dataa (Seperated by ',')").split(",")
            age = int(age)
            height = int(height)
            if height<1 and age<1:
                raise ValueError("Nagetive Number :")
            lst = [name,age,height]
        except Exception as e:
            print("Invalid Input :",e)
        else :
            break
    List.append(tuple(lst))
List.sort()
print(List)