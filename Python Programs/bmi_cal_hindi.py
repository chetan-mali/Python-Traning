while(True):
    try:
        height = float(input("\u0905\u092A\u0928\u093e \u0932\u092e\u094d\u092c\u093e\u0908 \u0926\u0930\u094d\u091c \u0915\u0930\u0947 :"))
        weight = float(input("\u0905\u092A\u0928\u093e \u0935\u091c\u0928 \u0926\u0930\u094d\u091c \u0915\u0930\u0947 :"))
        if(weight<1 or height<1):
            raise ValueError()
    except Exception:
        print("Invalid Input !!")
    else:
        break

BMI = weight/height**2
print("\u092c\u0940\u090f\u092e\u0906\u0908 :",BMI)
