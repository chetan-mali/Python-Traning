while(True):
    try:
        small_B,big_B,taget = map(int,input("Enter data seperated by space :").split())
        if(small_B<0 or big_B<0 or taget<0):
            raise ValueError("Nagetive Value ")
    except Exception as e:
        print("Invalid Input:" ,e)
    else:
        break
flag=0
for brick1 in range(1,small_B+1):
    for brick2 in range(1,big_B+1):
        if (brick1*1+brick2*5)== taget:
            flag = 1
if flag==1:
    print("True")
else:
    print("False")

