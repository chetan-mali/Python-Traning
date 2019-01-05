def check(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if temp==rev:
        return True
flag=0
list1 = [12,61,12,12,14]
for i in list1:
    if i<0:
        print("False")
        exit()
for i in list1:
    if check(i)== True:
        flag=1
if flag==1:
    print("True")
else:
    print("False")