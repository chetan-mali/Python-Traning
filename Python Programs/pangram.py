alphabet = [chr(ord('a')+i) for i in range(0,26)]
flag=1
string = input("Enter a string :")
string = string.lower()
for charater in alphabet:
    if charater not in string:
        flag=0;
if flag == 0 :
    print("NOT PANGRAM ")
else:
    print("PANGRAM")
