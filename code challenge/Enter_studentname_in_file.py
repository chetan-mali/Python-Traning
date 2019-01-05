while(True):
    try:
        file = open("student.txt","w")
        for _ in range(1,6):
            name = input("Student Name %d :"%_)
            file.write(name+"\n")
    except Exception as e:
        print(e)
    else:
        break
    finally:
        file.close()
print("Successfully !!!")