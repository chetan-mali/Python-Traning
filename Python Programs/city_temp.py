while(True):
    try:
        temperature = int(input("Enter Temperature :"))
    except ValueError as e:
        print("Invalid Input !!!")
    else:
        break
print(temperature,"\u00b0 C",sep='')