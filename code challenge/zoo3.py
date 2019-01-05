#calculate water need by individual animal [zoo.csv]
while(True):
    try:
        file = open("zoo.csv","r")
        List = file.readlines()
        animal_dict = {'elephant':0,'zebra':0,'kangaroo':0,'tiger':0}
        for data in List:
            data = list(data.split(","))
            if data[0] in animal_dict.keys():
                animal_dict[data[0]]+=int(data[2])
    except Exception as e:
        print(e)
    else:
        break
    finally:
        file.close()
print("Water Need :")
for key,value in animal_dict.items():
    print("   ",key ,":",value)