#Print data of CSV file (Zoo.csv)
while(True):
    try:
        filename = input("Enter name of file you want to Read :")
        file_open = open(filename,"r")
        List = file_open.readlines()
        for data in List:
            print(data,end="")
    except Exception as e:
        print(e)
    else:
        break
    finally:
        file_open.close()