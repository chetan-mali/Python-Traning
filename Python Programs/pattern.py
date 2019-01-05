while(True):
    try:
        number = int(input("Enter number :"))
        if number<0:
            raise ValueError("Nagetive Number")
    except Exception as e:
        print("Invalid Input:",e)
    else:
        break
[print('*'*n) for n in range(number+1)]
[print('*'*n) for n in range(number-1,0,-1)]