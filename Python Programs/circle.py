import math
while(True):
    try:
        radius = float(input("Enter Radius of circle :"))
        if(radius<1):
            raise ValueError()
    except  Exception:
        print("Invalid input !!")
    else:
        break
area_circle = math.pi*radius**2
print("Area of Circle :%.2f"%area_circle)
print("Perimeter of circle :%.2f"%(2*math.pi*radius))