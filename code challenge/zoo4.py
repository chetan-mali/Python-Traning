# calculate water need by all Animals
Sum =0
while(True):
    try:
        file = open("zoo.csv","r")
        List = file.readlines()
        for data in List:
            data = list(data.split(","))
            if data[2]!='water_need\n':
                Sum+=int(data[2])
    except Exception as e:
        print(e)
    else:
        break
    finally:
        file.close()
print("Water Need For All Animals:",Sum)