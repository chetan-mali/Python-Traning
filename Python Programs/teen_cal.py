def fix_teen(number):
    if number>=13 and number<=19 and number!=15 and number!=16:
        return 0
    else:
        return number

dict_data={}
Sum = 0
while(True):
    try:
        for count in range(3):
            key,value = input().split()
            value = int(value)
            dict_data[key]=value
    except Exception :
        print("Invalid Input !!")
    else:
        break
for key,value in dict_data.items():
    Sum += fix_teen(value)
print("Sum =",Sum)