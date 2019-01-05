while(True):
    try:
        user_input = list(map(int,input("Enter numbers (seperated by ',')").split(",")))
    except Exception:
        print("Invalid Input !!!")
    else:
        break
Sum =0
element =0
while(element < len(user_input)):
    if user_input[element] == 13:
        element+=2
    else:
        Sum+=user_input[element]
        element+=1
print(Sum)