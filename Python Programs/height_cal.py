# Calculate the age in meter and centimeter......
while(True):
    try:
        foot,inch = map(int,input("Enter height in foot and inch seperated by space :").split())
        if(foot<0 or inch<0):
            raise ValueError("Height can't be nagetive !!")
    except ValueError as e :
        print("Invalid Input :",e,"\n")
    else:
        break

h_meter = (foot*0.3048)+(inch*0.0254)            #convertion of height into meter
h_cm = h_meter*100                               #convertion of height into centimerter

print("Height in Meter : ",h_meter)
print("Height in Centimeter : ",h_cm)
