import math
while(True):
    try:
        number = int(input("Enter a number :"))
        if(number<1):
            raise ValueError("Nagetive Number !!")
    except ValueError as e:
        print("Invalid Input :",e)
    else:
        break

print("Factorial of Number is :",math.factorial(number))