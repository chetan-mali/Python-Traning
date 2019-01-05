while(True):
    try:
        user_input = list(map(int,input("Enter numbers (seperated by ',')").split(",")))
    except Exception:
        print("Invalid Input !!!")
    else:
        break
user_input.sort()
print((sum(user_input[1:-1]))/(len(user_input)-2))