while(True):
    try:
        weight,height=map(int,input("Enter weight and height in KG and meter(seperated by space):").split())
        if(weight<1 or height<1):
            raise ValueError("weight or height can't be nagetive or zero !!")
    except ValueError as e:
        print("Invalid input :",e,"\n")
    else:
        break

BMI=(weight/height)/height                   #calculation of BMI
print("BMI is:",BMI)
