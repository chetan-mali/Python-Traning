#print selected data form csv file (zoo.csv) names of :[animals]
while(True):
    try:
        file = open("zoo.csv","r")
        List = file.readlines()
        for data in List:
            data = list(data.split(","))
            print(data[0])
    except Exception as e:
        print(e)
    else:
        break
    finally:
        file.close()